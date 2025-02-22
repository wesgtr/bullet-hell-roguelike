import arcade
import random
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Dimension Shift: Bullet Hell Roguelike"

class DimensionShiftGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.all_sprites = None
        self.bullets = None
        self.enemies = None
        self.enemy_bullets = None
        self.enemy_spawn_timer = 0
        self.shoot_sound = arcade.load_sound("assets/laser.mp3")
        self.enemy_shoot_sound = arcade.load_sound("assets/laser2.mp3")
        

    def setup(self):
        self.player = Player()
        self.all_sprites = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.enemy_bullets = arcade.SpriteList()
        self.all_sprites.append(self.player)
        self.spawn_enemy()

        x = random.randint(100, SCREEN_WIDTH - 100)
        y = random.randint(300, SCREEN_HEIGHT - 100)
        enemy = Enemy(x, y)
        self.enemies.append(enemy)
        self.all_sprites.append(enemy)
        
        
    def spawn_enemy(self):
        """Spawn an enemy at a random position at the top of the screen."""
        if len(self.enemies) < 5:  # Check if the number of enemies is less than the maximum allowed
            enemy = Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.enemies.append(enemy)
            self.all_sprites.append(enemy)

    def on_draw(self):
        self.clear()
        self.all_sprites.draw()
        self.bullets.draw()
        self.enemy_bullets.draw()

    def on_update(self, delta_time):
        self.all_sprites.update()
        self.bullets.update()
        self.enemy_bullets.update()
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

        for enemy in self.enemies:
            bullet = enemy.shoot(self.player.center_x, self.player.center_y)
            if bullet:
                self.enemy_bullets.append(bullet)
                self.all_sprites.append(bullet)
                arcade.play_sound(self.enemy_shoot_sound)

        for bullet in self.enemy_bullets:
            if arcade.check_for_collision(bullet, self.player):
                bullet.kill()
                # Handle player hit (e.g., reduce health, end game, etc.)
                self.player.health -= 1
                

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = -self.player.speed
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = self.player.speed
        elif key in (arcade.key.UP, arcade.key.W):
            self.player.change_y = self.player.speed
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.player.change_y = -self.player.speed

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.player.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S):
            self.player.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            bullet = Bullet(self.player.center_x, self.player.center_y, x, y)
            self.bullets.append(bullet)
            self.all_sprites.append(bullet)
            arcade.play_sound(self.shoot_sound)
