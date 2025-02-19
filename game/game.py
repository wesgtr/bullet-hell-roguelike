import arcade
from game.player import Player
from game.bullet import Bullet

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
        self.bullets = None

    def setup(self):
        """Initializes the game."""
        self.player = Player()
        self.all_sprites = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.all_sprites.append(self.player)

    def on_draw(self):
        """Render the game."""
        self.clear()
        self.all_sprites.draw()
        self.bullets.draw()

    def on_update(self, delta_time):
        """Update game logic."""
        self.all_sprites.update()
        self.bullets.update()

    def on_key_press(self, key, modifiers):
        """Handle key presses (movement)."""
        if key in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = -self.player.speed
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = self.player.speed
        elif key in (arcade.key.UP, arcade.key.W):
            self.player.change_y = self.player.speed
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.player.change_y = -self.player.speed

    def on_key_release(self, key, modifiers):
        """Handle key releases (stop movement)."""
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.player.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S):
            self.player.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """Rotate player towards the mouse."""
        self.player.rotate_towards_mouse(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        """Shoot a bullet towards the mouse position."""
        if button == arcade.MOUSE_BUTTON_LEFT:
            bullet = Bullet(self.player.center_x, self.player.center_y, x, y)
            self.bullets.append(bullet)
            self.all_sprites.append(bullet)

