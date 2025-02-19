import arcade
import math

PLAYER_SPEED = 5

class Player(arcade.Sprite):
    """Player class."""

    def __init__(self):
        super().__init__("assets/player.png", 0.5)  # Placeholder sprite
        self.center_x = 400
        self.center_y = 300
        self.change_x = 0
        self.change_y = 0
        self.speed = PLAYER_SPEED

    def update(self, delta_time: float = 1/60):
        """Update player movement."""
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Keep player within screen bounds
        if self.left < 0:
            self.left = 0
        if self.right > 800:
            self.right = 800
        if self.bottom < 0:
            self.bottom = 0
        if self.top > 600:
            self.top = 600

    def rotate_towards_mouse(self, mouse_x, mouse_y):
        """Rotate the player towards the mouse cursor."""
        dx = mouse_x - self.center_x
        dy = mouse_y - self.center_y
        self.angle = math.degrees(math.atan2(dy, dx)) - 90  # Adjust sprite rotation
