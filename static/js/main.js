import { 
    setUsername, 
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
        const usernameModal = document.getElementById('username-modal');
        username = document.getElementById('username').value;
        if (username) {
            setUsername(username);
            usernameModal.show = false;
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
        chatBox.value += `\n${username}\t - ${data}`;
        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    });
})()