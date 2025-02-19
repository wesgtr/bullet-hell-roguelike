import arcade
import os


# the game setup 
WIDTH = 1280
HEIGHT = 720
FPS = 60

# The player settings 
PLAYER_START_X = 400
PLAYER_START_Y = 500
PLAYER_SIZE = 0.35
PLAYER_SPEED = 10

# The monster stats
monster_data = {
    "Runestones": {"health": 100, "attack_damage": 20, "roaming_speed": 2, "hunting_speed": [4, 4, 7, 7, 7], "image": arcade.image.load("placeholder"), "image_scale": 1.5, "hitbox": arcade.Rect(0, 0, 75, 100), "animation_speed": 0.2, "roaming_animation_speed": 0.05, "death_animation_speed": 0.12, "notice_radius": 600}
}