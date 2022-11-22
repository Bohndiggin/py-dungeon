def the_peeper(x_max, y_max, rooms): # looks up down right and left for room for a room
    directions = ['north', 'south', 'east', 'west']
    #find the next cut off either end of dungeon or other room.
    previous_room = rooms[-1]
    """
    Options for looking for obstructions
    A. Create array of scene fill occupied spaces with 1
    B. Or an array of just the occupied spaces, no 0s
    C. Or array of ranges of occupied spaces - smaller
    D. Math+coordinates to determine closest blocks.
    E. 
    """
    occupied = []
    for room in rooms:
        x_range = [room.x_axis_start, room.x_axis_end]
        y_range = [room.y_axis_start, room.y_axis_end]
        occupied.append([x_range, y_range])
    pass

def hallway_connector(room1, room2):
    room1.connected_rooms.append(room2)
    room2.connected_rooms.append(room1)