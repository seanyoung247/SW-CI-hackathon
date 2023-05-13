from os import environ
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
socketio = SocketIO(app)


# Entry point. Loads the index.html
@app.route('/')
def index():
    return render_template('index.html')

PLAYERS = {}

# Socket two way communications between clients and server --

# Username admin
@socketio.on('set-username')
def set_username(message):
    # Add the new username to the session
    PLAYERS[request.sid]['username'] = message['username']
    # Put the player in the waiting room
    PLAYERS[request.sid]['arena'] = 'waiting'
    join_room(PLAYERS[request.sid]['arena'])


# Arena admin
@socketio.on('get-challenge-code')
def get_challenge_code():
    emit('my-code', {'code': request.sid})


@socketio.on('challenge-player')
def challenge_player(message):

    # You aint Jekyll and Hyde! You can't challenge yourself!
    if message['code'] == request.sid:
        emit('challenge-failed', {'data':"You can't challenge yourself!"})
        return
    
    # Does the player we're challenging even exist?
    if message['code'] not in PLAYERS:
        emit('challenge-failed', {'data':"Invalid challenge code!"})
        return
    
    # Is the player we're challenging free?
    if PLAYERS[message['code']].get('challenger'):
        emit('challenge-failed', {'data':"Player already dueling!"})
        return
    
    # Lets get ready to ruuuuuumble







# Basic client server admin
@socketio.on('connect')
def sock_connect():
    print('Client connected')
    PLAYERS[request.sid] = {
        'username': None,
        'arena': None,
        'challenger': None,
    }
    emit('recieve', {'type': 'admin', 'data': 'Connected'})


@socketio.on('disconnect')
def sock_disconnect():
    # We need to clear the challenger if set
    challenger =  PLAYERS[request.sid].get('challenger')
    if challenger:
        PLAYERS[challenger]['challenger'] = None
        PLAYERS[challenger]['waiting']
        emit('chat-msg', {
            'user': PLAYERS[request.sid].get('username'),
            'data': 'Has Left'
        })

    del PLAYERS[request.sid]
    print('Client disconnected')


@socketio.on('test-session')
def test_session():
    print(PLAYERS.get(request.sid).get('username'))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
