import { socket, joinArena, leaveArena, sendChat } from './sockets.js';

(()=>{

    const roomInput = document.getElementById('room-name');
    const userInput = document.getElementById('username');
    let room = '';

    document.getElementById('join-room').addEventListener('click', e => {
        const roomID = roomInput.value;
        if (roomID) {
            room = roomID;
            joinArena(userInput.value, room);
        }
    });

    document.getElementById('leave-room').addEventListener('click', e => {
        if (room) {
            leaveArena(userInput.value, room);
        }
    });

    document.getElementById('chat').addEventListener('submit', e => {
        e.preventDefault();
        const user = userInput.value;
        const msg = document.getElementById('chat-msg').value;
        sendChat(user, msg, room);
    });

    socket.on('chat-msg', msg => {
        console.log(msg.username, msg.data);
    })

})()