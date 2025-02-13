import arcade

class Bullet(arcade.Sprite):
    """Bullet class."""

    def __init__(self, x, y):
        super().__init__("assets/bullet.png", 0.5)
        self.center_x = x
        self.center_y = y
        self.change_y = 10

    def update(self):
        """Move bullet upwards."""
        self.center_y += self.change_y
        if self.top > 600:
            self.kill()
