from flask_socketio import emit, join_room, leave_room
from defs import CHARACTERS


def set_arena(player, arena):
    if player['arena'] and player['arena'] != player['id']:
        leave_room(player['arena'], sid=player['id'])
    
    player['arena'] = arena
    join_room(player['arena'], sid=player['id'])


def set_challenger(player, challenger):
    # Put players in a private room
    set_arena(challenger, player['id'])
    set_arena(player, player['id'])
    # Set challengers
    player['challenger'] = challenger
    challenger['challenger'] = player
    # Clear round stats
    player['round_stats'] = None
    challenger['round_stats'] = None
    # Set battle start vars
    player['health'] = CHARACTERS[player['character']]['health']
    challenger['health'] = CHARACTERS[challenger['character']]['health']


def end_challenge(player, challenger):
    set_arena(challenger, 'waiting')
    set_arena(player, 'waiting')
    player['challenger'] = None
    player['round_stats'] = None
    challenger['challenger'] = None
    challenger['round_stats'] = None
    player['health'] = 0
    challenger['health'] = 0