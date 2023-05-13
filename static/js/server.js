
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





// // Join Room
// export function joinArena(username, arena) {
//     socket.emit('join-arena', {username, arena});
// }

// // Leave Room
// export function leaveArena(username, arena) {
//     socket.emit('leave-arena', {username, arena});
// }

// // Send chat
// export function sendChat(username, message, arena) {
//     socket.emit('chat-msg', {username, message, arena});
// }

// Recieve chat
export function recieveChat() {}