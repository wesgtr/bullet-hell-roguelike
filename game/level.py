import arcade
import random
from enemy import Enemy
from floor_gen import FloorGenerator

class Room:
    def __init__(self, width, height, is_boss_room=False):
        self.width = width
        self.height = height
        self.is_boss_room = is_boss_room
        self.doors = {}  # Dictionary to store door connections ("north", "south", etc.)
        self.enemies = arcade.SpriteList()  # List of enemies in the room
        self.locked = False  # Whether the room is locked
        self.background = None  # To hold the background image for the room
    
    def add_door(self, direction, room):
        """Connect this room to another room in the given direction."""
        self.doors[direction] = room
    
    def spawn_enemies(self):
        """Spawn enemies based on room type."""
        enemy_count = 5 if self.is_boss_room else random.randint(1, 3)
        for _ in range(enemy_count):
            enemy = Enemy(random.randint(50, self.width - 50), random.randint(50, self.height - 50))
            self.enemies.append(enemy)
        self.locked = True  # Lock the room when enemies are present
    
    def defeat_enemy(self, enemy):
        """Remove an enemy from the room."""
        if enemy in self.enemies:
            enemy.kill()
        if len(self.enemies) == 0:
            self.locked = False  # Unlock when all enemies are defeated

    def on_draw(self):
        """Draw the room with the background image."""
        if self.background:
            arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, arcade.load_texture(self.background))

    def check_collision(self, sprite):
        """Check if a sprite is within the room's perimeter."""
        if sprite.left < 0:
            sprite.left = 0
        if sprite.right > self.width:
            sprite.right = self.width
        if sprite.bottom < 0:
            sprite.bottom = 0
        if sprite.top > self.height:
            sprite.top = self.height

class Level:
    def __init__(self):
        self.rooms = []
        self.floor_generator = FloorGenerator(1280, 720)  # Screen size
        self.generate_rooms()
    
    def generate_rooms(self):
        """Create and connect rooms procedurally."""
        rooms = self.floor_generator.get_rooms()
        boss_room = Room(800, 800, is_boss_room=True)
        rooms.append(boss_room)
        random.shuffle(rooms)  # Shuffle for variety
        
        for i in range(len(rooms) - 1):
            direction = random.choice(["north", "south", "east", "west"])
            rooms[i].add_door(direction, rooms[i + 1])
            opposite = {"north": "south", "south": "north", "east": "west", "west": "east"}[direction]
            rooms[i + 1].add_door(opposite, rooms[i])
        
        self.rooms = rooms
        for room in self.rooms:
            room.spawn_enemies()
    
    def get_start_room(self):
        """Return the first room as the starting point."""
        return self.rooms[0]
