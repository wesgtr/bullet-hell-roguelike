import arcade
from game.player import Player

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dimension Shift: Bullet Hell Roguelike"

class DimensionShiftGame(arcade.Window):
    """Main game class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.all_sprites = None

    def setup(self):
        """Initializes the game."""
        self.player = Player()
        self.all_sprites = arcade.SpriteList()
        self.all_sprites.append(self.player)

    def on_draw(self):
        """Render the game."""
        self.clear()
        self.all_sprites.draw()

    def on_update(self, delta_time):
        """Update game logic."""
        self.all_sprites.update()

    def on_key_press(self, key, modifiers):
        """Handle key presses."""
        if key == arcade.key.LEFT:
            self.player.change_x = -self.player.speed
        elif key == arcade.key.RIGHT:
            self.player.change_x = self.player.speed
        elif key == arcade.key.UP:
            self.player.change_y = self.player.speed
        elif key == arcade.key.DOWN:
            self.player.change_y = -self.player.speed
        elif key == arcade.key.SPACE:
            self.shoot()

    def on_key_release(self, key, modifiers):
        """Handle key releases."""
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0

    def shoot(self):
        """Player shoots a bullet."""
        bullet = Bullet(self.player.center_x, self.player.top)
        self.all_sprites.append(bullet)
