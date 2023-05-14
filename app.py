from os import environ
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from utils import set_arena, set_challenger, end_challenge
from game import create_stat_sheet, resolve_round
from defs import CHARACTERS, WEAPONS, MODIFIERS

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
socketio = SocketIO(app)


PLAYERS = {}


# Entry point. Loads the index.html
@app.route('/')
def index():
    return render_template(
        'index.html', 
        characters=CHARACTERS, 
        weapons=WEAPONS, 
        modifiers=MODIFIERS
    )


# Socket two way communications between clients and server --

# Game details
@socketio.on('get-objects')
def get_objects():
    emit('set-objects', {
        'characters': CHARACTERS, 
        'weapons': WEAPONS, 
        'modifiers': MODIFIERS
    })

# Username admin
@socketio.on('set-username')
def set_username(message):
    # Add the new username to the session
    PLAYERS[request.sid]['username'] = message.get('username')
    # Put the player in the waiting room
    set_arena(PLAYERS[request.sid], 'waiting')


# Character
@socketio.on('set-character')
def set_character(message):
    PLAYERS[request.sid]['character'] = message.get('character')


# Arena admin
@socketio.on('get-challenge-code')
def get_challenge_code():
    emit('my-code', {'code': request.sid})


@socketio.on('challenge-player')
def challenge_player(message):

    # Did we maybe forget something?
    if not message.get('code'):
        emit('challenge-failed', {'data':"No challenge code"})
        return

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
    emit('challenge-accepted', {
        'players': [
            {
                'id': player['id'],
                'username': player['username'],
                'character': player['character'],
                'health': player['health'],
            },
            {
                'id': challenger['id'],
                'username': challenger['username'],
                'character': challenger['character'],
                'health': challenger['health'],
            }
        ]
    }, broadcast=True)


@socketio.on('leave-challenge')
def leave_challenge():
    # You're a do not person then, huh?
    player = PLAYERS[request.sid]
    challenger = PLAYERS[player['challenger']]
    end_challenge(player, challenger)


# Battle routes
@socketio.on('do-round')
def do_round(message):
    player = PLAYERS[request.sid]
    challenger = player['challenger']
    
    if not challenger:
        emit('round-failed', {'data': 'No challenger'})
        return
    
    if not all(keys in message for keys in ('character','weapon','modifier')):
        emit('round-failed', {'data': 'Missing required fields'})

    # Generate the round sheet for the current player
    player['round_stats'] = create_stat_sheet(
        player,
        message['character'],
        message['weapon'],
        message['modifier'],
    )
    
    # Do we have a round sheet for the challenger yet?
    if challenger['round_stats']:
        # Do fight
        result = resolve_round(player, challenger)
        # Check who won
        # Broadcast results back to players

        # If battle has been won, end the challenge 
        # and return players to waiting room


    # Else wait for challenger
    return


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
        'character': None,      # Name of the player character
        'arena': None,          # The Players current room
        'challenger': None,     # The Players current challenger
        'health': 0,            # Player current health
        'round_stats': None,    # The Players calculated stats for the current round
    }
    emit('recieve', {'type': 'admin', 'data': 'Connected'})


@socketio.on('disconnect')
def sock_disconnect():
    # We need to clear the challenger if set
    challenger =  PLAYERS[request.sid].get('challenger')
    if challenger:
        end_challenge(PLAYERS[request.sid], challenger)

    del PLAYERS[request.sid]
    print('Client disconnected')


@socketio.on('test-session')
def test_session():
    print(PLAYERS.get(request.sid).get('username'))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
