import arcade

PLAYER_SPEED = 5

class Player(arcade.Sprite):
    """Player class."""

    def __init__(self):
        super().__init__("assets/player.png", 0.2)
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
        if self.right > 1280:
            self.right = 1280
        if self.bottom < 0:
            self.bottom = 0
        if self.top > 720:
            self.top = 720
