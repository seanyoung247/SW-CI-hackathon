from flask_socketio import SocketIO, emit, join_room, leave_room, rooms


def set_arena(player, arena):
    if player['arena']:
        leave_room(player['arena'])
    
    player['arena'] = arena
    join_room(player['arena'])