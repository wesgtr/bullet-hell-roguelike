import arcade

class Enemy(arcade.Sprite):
    """Enemy class."""

    def __init__(self, x, y):
        super().__init__("assets/enemy.png", 0.2)
        self.center_x = x
        self.center_y = y
        self.change_y = -2

    def update(self, delta_time: float = 1/60):
        """Move the enemy down."""
        self.center_y += self.change_y
        if self.bottom < 0:
            self.kill()
