
// IO from "https://cdn.socket.io/4.6.0/socket.io.min.js"
export const socket = io();

// FUNCTIONS THAT I NEED:

// Connect/Disconnect

// Join Room
export function joinArena(username, arena) {
    console.log(username, arena);
    socket.emit('join-arena', {username, arena});
}

// Leave Room
export function leaveArena(username, arena) {
    socket.emit('leave-arena', {username, arena});
}

// Send chat
export function sendChat(username, message, arena) {
    socket.emit('chat-msg', {username, message, arena});
}
