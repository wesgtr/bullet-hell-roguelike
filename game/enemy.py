import arcade
import random
import math

ENEMY_SPEED = 2
BULLET_SPEED = 5
ENEMY_SHOOT_INTERVAL = 4.0

class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        enemy_image = f"assets/enemy{random.randint(1, 3)}.png"
        super().__init__(enemy_image, 0.1)
        self.center_x = x
        self.center_y = y
        self.change_x = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.change_y = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.time_since_last_shot = 0

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 1280:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 720:
            self.change_y *= -1

        self.time_since_last_shot += delta_time

    def shoot(self, player_x, player_y):
        if self.time_since_last_shot >= ENEMY_SHOOT_INTERVAL:
            self.time_since_last_shot = 0

            dx = player_x - self.center_x
            dy = player_y - self.center_y
            angle = math.atan2(dy, dx)

            return Bullet(self.center_x, self.center_y, angle)
        return None

class Bullet(arcade.Sprite):
    def __init__(self, x, y, angle):
        super().__init__("assets/bullet2.png", 0.01)
        self.center_x = x
        self.center_y = y
        self.change_x = math.cos(angle) * BULLET_SPEED
        self.change_y = math.sin(angle) * BULLET_SPEED
        self.angle = math.degrees(angle)

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x < 0 or self.center_x > 1280 or self.center_y < 0 or self.center_y > 720:
            self.kill()
