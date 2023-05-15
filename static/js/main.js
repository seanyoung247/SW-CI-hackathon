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
        health: 0,
    };
    // Stores the details of the remote challenger
    const challenger = {
        id: '',
        username: '',
        character: '',
        health: 0,
    };

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
        // Indicate battle has started...
    });

    /*
     * Fired when round has ended without a winner
     */
    onRoundEnd(msg => {
        console.log('round complete');
        console.log(msg);
    });

    /*
     * Fired when battle is complete and there is a winner
     */
    onBattleEnd(msg => {
        console.log('Battle complete');
        console.log(msg.winner, msg.players);
    });


    // TEMPORARY FOR TESTING BATTLE ROUNDS
    document.getElementById('test').addEventListener('click', e => {
        // TEST
        doRound(user.character, objects.characters[user.character].weapon, 'strength');
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
        // TEMPORARY. NEEDS TO BE SET BY CHARACTER CHOOSER UI
        user.character = document.getElementById('characterName').value;

        if (user.character) {
            setCharacter(user.character);
            characterModal.show = false;
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
        const chatBox = document.getElementById('chat-box');
        const {username, data} = msg;
        // Add the message
        chatBox.value += `${username}\t - ${data}\n`;
        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    });
})()