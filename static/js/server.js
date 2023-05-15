
// IO from "https://cdn.socket.io/4.6.0/socket.io.min.js"
export const socket = io();

// FUNCTIONS THAT I NEED:

// Connect/Disconnect


/*
 * Player management
 */
export function setUsername(username) {
    socket.emit('set-username', {username});
}

export function getObjects() {
    return new Promise( resolve => {
        socket.emit('get-objects');
        socket.on('set-objects', resolve);
    });
}

export function getChallengeCode() {
    return new Promise( resolve => {
        socket.emit('get-challenge-code');
        socket.on('my-code', msg => resolve(msg.code));
    });
}


/*
 * Character management
 */
export function setCharacter(character) {
    socket.emit('set-character', {character});
}


/*
 * Challenges/Battles
 */
export function challengePlayer(code) {
    return new Promise( (resolve, reject) => {
        if (!code) reject('No code specified');
        socket.emit('challenge-player', {code});

        socket.on('challenge-accepted', msg => resolve(msg));
        socket.on('challenge-failed', msg => reject(msg.data));
    });
}

export function endChallenge() {
    socket.emit('leave-challenge');
}


/*
 * Battle Rounds
 */
export function doRound(character, weapon, modifier) {
    socket.emit('do-round', {character, weapon, modifier});
}


/*
 * Chat messages
 */
export function sendChat(message) {
    socket.emit('chat-msg', message);
}

export function recieveChat(callback) {
    socket.on('chat-msg', callback);
}


/*
 * Events
 */
export function onConnect(callback) {
    socket.on('connect', callback);
}

export function onChallenge(callback) {
    socket.on('challenge-accepted', callback);
}

export function onRoundEnd(callback) {
    socket.on('round-complete', callback);
}

export function onBattleEnd(callback) {
    socket.on('battle-complete', callback);
}
