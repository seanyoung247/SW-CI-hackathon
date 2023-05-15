import { 
    setUsername, setCharacter, getChallengeCode, getObjects,    // Setup
    onChallenge, onBattleEnd, onRoundEnd, onConnect,            // Events
    challengePlayer, endChallenge,                              // Challenges
    sendChat, recieveChat,                                      // Chat
    doRound                                                     // Battle rounds
} from './server.js';

(()=>{
    // Stores the object definitions from the server
    const objects = {
        characters: null,
        weapons: null,
        modifiers: null,
    };

    // Stores the details of the local player
    const user = {
        id: '',
        username: '',
        character: '',
        deck: null,
        health: 0,
    };
    // Stores the details of the remote challenger
    const challenger = {
        id: '',
        username: '',
        character: '',
        health: 0,
    };
    const startRoundBtn = document.getElementById('start-round-btn');

    function addToChat(msg) {
        const chatBox = document.getElementById('chat-box');
        // Add the message
        chatBox.value += `${msg}\n`;
        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    }


    function setCharacterCard(character, which) {
        const card = document.getElementById(`${which}-card`);
        const visible = document.querySelector(`#${which}-card > div`);
        const playerName = document.getElementById(`${which}-name`);
        const playerImg = document.getElementById(`${which}-img`);
        const strengthStat = document.getElementById(`${which}-str-value`);
        const skillStat = document.getElementById(`${which}-ws-value`);
        const agilityStat = document.getElementById(`${which}-agi-value`);
        const healthStat = document.getElementById(`${which}-health-value`);

        const charStats = objects.characters[character];

        playerName.innerText = charStats.name;
        playerImg.src = 'static/' + charStats.image;
        strengthStat.innerText = parseInt(charStats.strength);
        skillStat.innerText = parseInt(charStats.skill);
        agilityStat.innerText = parseInt(charStats.agility);
        healthStat.innerText = parseInt(charStats.health);

        card.classList.remove('sith');
        card.classList.remove('jedi');
        card.classList.add(charStats.affiliation);

        visible.classList.remove('hide');
        visible.classList.add('show');
    }


    function getRandomCards(deck) {
        for(let i = deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i+1));
            [deck[i], deck[j]] = [deck[j], deck[i]];
        }
        return deck;
    } 

    function showChallengeCode(code) {
        user.id = code;
        document.getElementById('player-challenge-code').innerText = code;
    }

    onConnect(msg => {
        if (msg && msg.code) showChallengeCode(msg.code);
        // Are there details to resend to the server?
        if (!user.id) {
            user.id = msg.code;
        } else {
            setUsername(user.username);
            setCharacter(user.character);
        }
    });

    /*
     * Gets the game object definitions from the server
     */
    getObjects()
        .then(msg => {
            objects.characters = msg.characters;
            objects.weapons = msg.weapons;
            objects.modifiers = msg.modifiers;
        });

    /*
     * Tries to challenge another user using their challenge code
     */
    document.getElementById('challenge-btn').addEventListener('click', e=> {
        const challengeInput = document.getElementById('challenge-code');
        const challengeCode = challengeInput.value;
        challengePlayer(challengeCode)
            .catch(msg => {
                challengeInput.value = '';
                alert(`Challenge failed: ${msg}`)
            });
    });

    /*
     * Fired on challenge/battle start
     */
    onChallenge(msg => {
        // Grab the player data:
        for (const player of msg.players) {
            if (player.id === user.id) {
                user.health = player.health;
            } else {
                challenger.id = player.id;
                challenger.username = player.username;
                challenger.character = player.character;
                challenger.health = player.health;
            }
        }
        setCharacterCard(challenger.character, 'challenger');
        alert(`You have a new challenger: ${challenger.username}`);
        startRoundBtn.disabled = false;
    });


    startRoundBtn.addEventListener('click', e => {
        // TEST!
        doRound(user.character, objects.characters[user.character].weapon, 'strength');

        startRoundBtn.disabled = true;

        addToChat(`Waiting for other player...`);
    });

    /*
     * Fired when round has ended without a winner
     */
    onRoundEnd(msg => {
        const chatBox = document.getElementById('chat-box');
        addToChat(`Round Complete!`);
        chatBox.scrollTop = chatBox.scrollHeight;
        startRoundBtn.disabled = false;
    });

    /*
     * Fired when battle is complete and there is a winner
     */
    onBattleEnd(msg => {
        addToChat(`Battle Complete!`);
        startRoundBtn.disabled = true;
    });

    /*
     * Sets user name
     */
    document.getElementById('set-user').addEventListener('click', e => {
        const usernameModal = document.getElementById('username-modal');
        user.username = document.getElementById('username').value;
        const characterModal = document.getElementById('character-modal');

        if (user.username) {
            setUsername(user.username );
            usernameModal.show = false;
            characterModal.show = true;
        }
    });


    /*
     * Sets player chracter
     */
    document.getElementById('set-character').addEventListener('click', e => {
        const characterModal = document.getElementById('character-modal'); 
        const characterSelect = document.getElementById('character-list');
        user.character = characterSelect.value;

        if (user.character) {
            setCharacter(user.character);
            characterModal.show = false;
            // Build player modifier deck
            user.deck = getRandomCards(objects.modifiers);
            // Fill out player card details
            setCharacterCard(user.character, 'player')
        }
    });

    /*
     * Sends chat messages to the current room or challenger
     */
    document.getElementById('chat').addEventListener('submit', e=>{
        const chatMsg = document.getElementById('chat-msg');
        e.preventDefault();
        if (chatMsg.value) {
            sendChat(chatMsg.value);
            // Clear chat message
            chatMsg.value = '';
        }
    });

    /*
     * Recieves messages from the current room or challenger
     */
    recieveChat(msg => {
        const {username, data} = msg;
        addToChat(`${username}\t - ${data}`);
    });
})()