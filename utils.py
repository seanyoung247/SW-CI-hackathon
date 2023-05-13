from flask_socketio import SocketIO, emit, join_room, leave_room, rooms


def set_arena(player, arena):
    if player['arena'] and player['arena'] != player['id']:
        emit('chat-msg', {
            'username': player['username'],
            'data': 'Has Left',
        }, to=arena, broadcast=True)
        leave_room(player['arena'])
    
    player['arena'] = arena
    join_room(player['arena'])
    print(player, player['arena'], player['username'])
    emit('chat-msg', {
        'username': player['username'],
        'data': 'Has joined',
    }, to=player['arena'], broadcast=True)



def set_challenger(player, challenger):
    pass
