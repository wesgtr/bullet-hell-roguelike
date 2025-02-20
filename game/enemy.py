import arcade
import random
import math

ENEMY_SPEED = 2
BULLET_SPEED = 5
ENEMY_SHOOT_INTERVAL = 4.0  # ✅ Agora claramente em segundos

class Enemy(arcade.Sprite):
    """Enemy class with random movement and shooting."""

    def __init__(self, x, y):
        enemy_image = f"assets/enemy{random.randint(1, 3)}.png"
        super().__init__(enemy_image, 0.1)
        self.center_x = x
        self.center_y = y
        self.change_x = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.change_y = random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.time_since_last_shot = 0
        self.has_shot = False  # ✅ Garante que só atire uma vez

    def update(self, delta_time: float = 1 / 60):
        """Moves the enemy randomly and checks if it should shoot."""
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 1280:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 720:
            self.change_y *= -1

        # ✅ Espera ENEMY_SHOOT_INTERVAL segundos para atirar
        if not self.has_shot:
            self.time_since_last_shot += delta_time
            if self.time_since_last_shot >= ENEMY_SHOOT_INTERVAL:
                self.has_shot = True  # ✅ Marca que o inimigo já atirou

    def shoot(self, player_x, player_y):
        """Dispara um tiro na direção do jogador, mas apenas uma vez."""
        if self.has_shot:  # ✅ Só atira se o tempo passou
            self.has_shot = False  # ✅ Impede novos tiros
            dx = player_x - self.center_x
            dy = player_y - self.center_y
            angle = math.atan2(dy, dx)  # ✅ Calcula a direção do jogador

            bullet = Bullet(self.center_x, self.center_y, angle)
            return bullet
        return None  # ✅ Retorna None se ainda não for hora de atirar

class Bullet(arcade.Sprite):
    """Bullet class for enemies."""

    def __init__(self, x, y, angle):
        super().__init__("assets/bullet2.png", 0.01)
        self.center_x = x
        self.center_y = y
        self.change_x = math.cos(angle) * BULLET_SPEED
        self.change_y = math.sin(angle) * BULLET_SPEED
        self.angle = math.degrees(angle)

    def update(self, delta_time: float = 1 / 60):
        """Move the bullet and remove if off-screen."""
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x < 0 or self.center_x > 1280 or self.center_y < 0 or self.center_y > 720:
            self.kill()
