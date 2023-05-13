from os import environ
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from utils import set_arena, set_challenger

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
socketio = SocketIO(app)


PLAYERS = {}


# Entry point. Loads the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Socket two way communications between clients and server --

# Username admin
@socketio.on('set-username')
def set_username(message):
    # Add the new username to the session
    PLAYERS[request.sid]['username'] = message['username']
    print( PLAYERS[request.sid]['username'], message['username'])
    # Put the player in the waiting room
    set_arena(PLAYERS[request.sid], 'waiting')


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
    
    player = PLAYERS[request.sid]
    challenger = PLAYERS[message['code']]
    # Lets get ready to ruuuuuumble
    set_challenger(player, challenger)


# Battle routes
@socketio.on('do-round')
def do_round():
    # Check if challenger has started round
        # Do fight
    # Else wait for challenger
    pass


# Chat routes
@socketio.on('chat-msg')
def chat_message(message):
    msg = {
        'username': PLAYERS[request.sid]['username'],
        'data': message,
    }
    emit('chat-msg', msg, to=PLAYERS[request.sid]['arena'], broadcast=True)



# Basic client server admin
@socketio.on('connect')
def sock_connect():
    print('Client connected')
    PLAYERS[request.sid] = {
        'id': request.sid,      # Player unique ID
        'username': None,       # Player display name
        'arena': None,          # The Players current room
        'challenger': None,     # The Players current challenger
        'ready': False,         # True if player is ready to start round
        # Player character and modifiers go here
    }
    emit('recieve', {'type': 'admin', 'data': 'Connected'})


@socketio.on('disconnect')
def sock_disconnect():
    # We need to clear the challenger if set
    challenger =  PLAYERS[request.sid].get('challenger')
    if challenger:
        PLAYERS[challenger]['challenger'] = None
        set_arena(PLAYERS[challenger], 'waiting')

    del PLAYERS[request.sid]
    print('Client disconnected')


@socketio.on('test-session')
def test_session():
    print(PLAYERS.get(request.sid).get('username'))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
