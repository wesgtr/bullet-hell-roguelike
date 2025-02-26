import arcade
import random

# Constants for room dimensions
ROOM_WIDTH = 600
ROOM_HEIGHT = 600
BOSS_ROOM_WIDTH = 800
BOSS_ROOM_HEIGHT = 800
BACKGROUND_IMAGE = "assets/background.png"

class Room:
    def __init__(self, width, height, is_boss_room=False):
        """Initialize a room with dimensions and boss status."""
        self.width = width
        self.height = height
        self.is_boss_room = is_boss_room
        self.background = None  # Delay loading texture until draw()

    def draw(self):
        """Draw the room's background and perimeter."""
        if not self.background:
            self.background = arcade.load_texture(BACKGROUND_IMAGE)  # Load only when needed

        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width, self.height, arcade.color.BLACK, 5)

class FloorGen:
    def __init__(self):
        """Initialize the floor generator with an empty room list."""
        self.rooms = []
        self.current_room = None  # Track the room the player is in

    def generate(self):
        """Create multiple rooms and store them in a list."""
        self.rooms = [Room(ROOM_WIDTH, ROOM_HEIGHT) for _ in range(9)]  # Generate 9 normal rooms
        boss_room = Room(BOSS_ROOM_WIDTH, BOSS_ROOM_HEIGHT, is_boss_room=True)  # Create a boss room
        self.rooms.append(boss_room)

        random.shuffle(self.rooms)  # Shuffle rooms for randomness
        self.current_room = self.rooms[0]  # Set the first room as the starting room

    def draw(self):
        """Draw the current room."""
        if self.current_room:
            self.current_room.draw()

    def get_current_room(self):
        """Return the current room."""
        return self.current_room
