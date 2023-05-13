import { 
    socket, setUsername, 
    getChallengeCode, challengePlayer,
    sendChat, recieveChat
} from './server.js';

(()=>{
    let username = '';
    let myId = '';


    /*
     * Gets the current users challenge code from the server
     */
    getChallengeCode()
        .then(code => {
            myId = code;
            document.getElementById('player-challenge-code').innerText = code;
        });

    /*
     * Tries to challenge another user using their challenge code
     */
    document.getElementById('challenge-btn').addEventListener('click', e=> {
        const challengeInput = document.getElementById('challenge-code');
        const challengeCode = challengeInput.value;
        challengePlayer(challengeCode)
            .then(()=>{

            })
            .catch(msg => {
                challengeInput.value = '';
                alert(`Challenge failed: ${msg}`)
            });
    });

    /*
     * Sets user name
     */
    document.getElementById('set-user').addEventListener('click', e => {
        username = document.getElementById('username').value;
        if (username) {
            setUsername(username);
        }
    });

    /*
     * Sends chat messages to the current room or challenger
     */
    document.getElementById('chat').addEventListener('submit', e=>{
        const chatMsg = document.getElementById('chat-msg').value;
        e.preventDefault();
        if (chatMsg) {
            sendChat(chatMsg);
        }
    });

    /*
     * Recieves messages from the current room or challenger
     */
    recieveChat(msg => {
        const chatBox = document.getElementById('chat-box');
        const {username, data} = msg;
        chatBox.value += `\n${username}\t - ${data}`;
    });
})()