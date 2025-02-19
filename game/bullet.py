import arcade
import math

BULLET_SPEED = 10

class Bullet(arcade.Sprite):
    """Bullet class."""

    def __init__(self, x, y, target_x, target_y):
        super().__init__("assets/bullet.png", 0.2)  # Placeholder sprite
        self.center_x = x
        self.center_y = y

        # Calculate direction
        dx = target_x - x
        dy = target_y - y
        angle = math.atan2(dy, dx)

        # Set velocity
        self.change_x = math.cos(angle) * BULLET_SPEED
        self.change_y = math.sin(angle) * BULLET_SPEED

        # Set rotation
        self.angle = math.degrees(angle) - 90

    def update(self, delta_time: float = 1/60):
        """Move the bullet."""
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Remove bullet if off-screen
        if self.center_x < 0 or self.center_x > 800 or self.center_y < 0 or self.center_y > 600:
            self.kill()
