import random

class Room:
    def __init__(self, x, y, room_type="normal"):
        self.x = x  # Room's X position in the grid
        self.y = y  # Room's Y position in the grid
        self.room_type = room_type
        self.neighbors = {}  # Stores room connections (N, S, E, W)

    def __repr__(self):
        return f"Room({self.x}, {self.y}, {self.room_type})"

def generate_dungeon():
    grid_size = 3  # 3x3 grid
    total_rooms = 10
    rooms = {}

    # Generate valid random positions for special rooms
    all_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    random.shuffle(all_positions)
    
    room_positions = {
        "start": all_positions.pop(),
        "shop": all_positions.pop(),
        "item1": all_positions.pop(),
        "item2": all_positions.pop(),
        "boss": all_positions.pop(),
    }

    # Create rooms with assigned types
    for r_type, pos in room_positions.items():
        rooms[pos] = Room(pos[0], pos[1], r_type)

    # Fill remaining spaces with normal rooms
    while len(rooms) < total_rooms:
        x, y = all_positions.pop()
        rooms[(x, y)] = Room(x, y, "normal")

    # Ensure connectivity (connect rooms to their neighbors)
    for (x, y), room in rooms.items():
        if (x, y - 1) in rooms:  # Connect to room below
            room.neighbors["S"] = rooms[(x, y - 1)]
        if (x, y + 1) in rooms:  # Connect to room above
            room.neighbors["N"] = rooms[(x, y + 1)]
        if (x - 1, y) in rooms:  # Connect to left room
            room.neighbors["W"] = rooms[(x - 1, y)]
        if (x + 1, y) in rooms:  # Connect to right room
            room.neighbors["E"] = rooms[(x + 1, y)]

    return rooms, room_positions["start"]  # Return dungeon and starting position 