
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

export function getChallengeCode() {
    return new Promise( resolve => {
        socket.emit('get-challenge-code');
        socket.on('my-code', msg => resolve(msg.code));
    });
}

export function challengePlayer(code) {
    return new Promise( (resolve, reject) => {
        if (!code) reject('No code specified');
        socket.emit('challenge-player', {code});

        socket.on('challenge-accepted', msg => resolve(msg));
        socket.on('challenge-failed', msg => reject(msg.data));
    });
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
