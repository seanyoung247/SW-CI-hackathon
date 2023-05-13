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
        const challenge_input = document.getElementById('challenge-code');
        const challenge_code = challenge_input.value;
        challengePlayer(challenge_code)
            .then(()=>{

            })
            .catch(msg => {
                challenge_input.value = '';
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