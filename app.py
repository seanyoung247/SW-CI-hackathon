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


# Room admin
@socketio.on('create-room')
def sock_create_room(message):
    pass


# Basic client server
@socketio.on('connect')
def sock_connect():
    emit('recieve', {'data': 'Connected'})


@socketio.on('disconnect')
def sock_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')