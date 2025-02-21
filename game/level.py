import arcade
from floor_gen import generate_dungeon

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROOM_SIZE = 200  # Virtual size of each room

class Dungeon:
    def __init__(self):
        self.rooms, start_position = generate_dungeon()
        self.current_room = self.rooms[start_position]  # Start at the correct room

    def move_player(self, direction):
        """Move the player to a connected room if possible"""
        if direction in self.current_room.neighbors:
            self.current_room = self.current_room.neighbors[direction]

class BulletHellRoguelike(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Dimension Shift")
        self.dungeon = Dungeon()

    def on_draw(self):
        arcade.start_render()
        self.draw_room()

    def draw_room(self):
        room = self.dungeon.current_room
        arcade.draw_text(f"Room Type: {room.room_type}", SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 50, arcade.color.WHITE, 20)
        arcade.draw_rectangle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 300, 300, arcade.color.GRAY_BLUE)

        # Draw connections to indicate movement
        if "N" in room.neighbors:
            arcade.draw_text("N", SCREEN_WIDTH//2, SCREEN_HEIGHT - 50, arcade.color.GREEN, 20)
        if "S" in room.neighbors:
            arcade.draw_text("S", SCREEN_WIDTH//2, 50, arcade.color.GREEN, 20)
        if "E" in room.neighbors:
            arcade.draw_text("E", SCREEN_WIDTH - 50, SCREEN_HEIGHT//2, arcade.color.GREEN, 20)
        if "W" in room.neighbors:
            arcade.draw_text("W", 50, SCREEN_HEIGHT//2, arcade.color.GREEN, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.dungeon.move_player("N")
        elif key == arcade.key.S:
            self.dungeon.move_player("S")
        elif key == arcade.key.A:
            self.dungeon.move_player("W")
        elif key == arcade.key.D:
            self.dungeon.move_player("E")

# Run the game
if __name__ == "__main__":
    game = BulletHellRoguelike()
    arcade.run()       
