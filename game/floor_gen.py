import arcade
import random
from game.level import Room  # Assuming Room class is in level.py

# Set the floor background image
FLOOR_BACKGROUND_IMAGE = "assets/background.png"

class FloorGenerator:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rooms = []
        self.generate_rooms()

    def generate_rooms(self):
        """Generate rooms with cobblestone floor background."""
        room_dimensions = [(600, 600), (600, 600), (600, 600)]  # 3 rooms for example

        # Create rooms with cobblestone floor background
        for width, height in room_dimensions:
            room = Room(width, height)
            room.background = FLOOR_BACKGROUND_IMAGE  # Set the background to cobblestone
            self.rooms.append(room)

    def get_rooms(self):
        """Return all generated rooms."""
        return self.rooms
