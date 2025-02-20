import random
import arcade
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Dimension Shift: Bullet Hell Roguelike"

class DimensionShiftGame(arcade.Window):
    """Main game class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.all_sprites = None
        self.bullets = None
        self.enemies = None
        self.shoot_sound = arcade.load_sound("assets/laser.mp3")
        self.enemy_spawn_timer = 0  # Add a timer attribute

    def setup(self):
        """Initializes the game."""
        self.player = Player()
        self.all_sprites = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()  # Initialize the enemies list
        self.all_sprites.append(self.player)
        self.spawn_enemy()

    def spawn_enemy(self):
        """Spawn an enemy at a random position at the top of the screen."""
        enemy = Enemy("assets/enemy.png", 0.5)
        enemy.center_x = random.randint(0, SCREEN_WIDTH)
        enemy.center_y = SCREEN_HEIGHT
        self.enemies.append(enemy)
        self.all_sprites.append(enemy)

    def on_draw(self):
        """Render the game."""
        self.clear()
        self.all_sprites.draw()
        self.bullets.draw()
        self.enemies.draw()

    def on_update(self, delta_time):
        """Update game logic."""
        self.all_sprites.update()
        self.bullets.update()
        self.enemies.update()

        # Check for bullet and enemy collisions
        for bullet in self.bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemies)
            for enemy in hit_list:
                bullet.kill()
                enemy.kill()

        # Update the enemy spawn timer
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer > 2:  # Spawn an enemy every 2 seconds
            self.spawn_enemy()
            self.enemy_spawn_timer = 0  # Reset the timer

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

    def on_mouse_press(self, x, y, button, modifiers):
        """Shoot a bullet towards the mouse position."""
        if button == arcade.MOUSE_BUTTON_LEFT:
            bullet = Bullet(self.player.center_x, self.player.center_y, x, y)
            self.bullets.append(bullet)
            self.all_sprites.append(bullet)
            arcade.play_sound(self.shoot_sound)

