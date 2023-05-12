from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # TEMP!
socketio = SocketIO(app)


# Entry point. Loads the index.html
@app.route('/')
def index():
    return render_template('index.html')


# Socket two way communications between clients and server --

# Chat messaging
@socketio.on('chat')
def sock_message(message):
    emit('receive', {'data': message['data']}, broadcast=True)


# Arena admin
@socketio.on('join-arena')
def sock_join_arena(message):
    username = message['username']
    arena = message['arena']
    join_room(arena)
    emit('chat-msg', {'username': username, 'data': 'has joined'}, to=arena)


@socketio.on('leave-arena')
def sock_leave_arena(message):
    username = message['username']
    arena = message['arena']
    leave_room(arena)
    emit('chat-msg', {'username': username, 'data': 'has left'}, to=arena)


# Chat
@socketio.on('chat-msg')
def sock_chat(message):
    username = message['username']
    arena = message['arena']
    msg = message['message']
    print(username, arena, msg)
    emit('chat-msg', {'username': username, 'data': msg}, broadcast=True, to=arena)


# Basic client server admin
@socketio.on('connect')
def sock_connect():
    emit('recieve', {'type': 'admin', 'data': 'Connected'})


@socketio.on('disconnect')
def sock_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')