from flask_socketio import SocketIO, emit, join_room, leave_room, rooms


def set_arena(player, arena):
    if player['arena'] and player['arena'] != player['id']:
        emit('chat-msg', {
            'username': player['username'],
            'data': 'Has Left',
        }, to=arena, broadcast=True)
        leave_room(player['arena'], sid=player['id'])
    
    player['arena'] = arena
    join_room(player['arena'], sid=player['id'])
    print(player, player['arena'], player['username'])
    emit('chat-msg', {
        'username': player['username'],
        'data': 'Has joined',
    }, to=player['arena'], broadcast=True)



def set_challenger(player, challenger):
    set_arena(challenger, player['id'])
    set_arena(player, player['id'])
    print(challenger['arena'], player['arena'])
    player['challenger'] = challenger['id']
    challenger['challenger'] = player['id']
