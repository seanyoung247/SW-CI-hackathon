import { socket, setUsername, getChallengeCode, challengePlayer } from './server.js';

(()=>{
    let username = '';
    let myId = '';


    getChallengeCode()
        .then(code => {
            myId = code;
            document.getElementById('player-challenge-code').innerText = code;
        });

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


    document.getElementById('set-user').addEventListener('click', e => {
        username = document.getElementById('username').value;
        if (username) {
            setUsername(username);
        }
    });
})()