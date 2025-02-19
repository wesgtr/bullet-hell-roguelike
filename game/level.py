import random
import arcade
from enemy import Enemy

class Room:
    def __init__(self, width, height, is_boss_room=False):
        self.width = width
        self.height = height
        self.is_boss_room = is_boss_room
        self.doors = {}  # Dictionary to store door connections ("north", "south", etc.)
        self.enemies = arcade.SpriteList()  # List of enemies in the room
        self.locked = False  # Whether the room is locked
    
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

class Level:
    def __init__(self):
        self.rooms = []
        self.generate_rooms()
    
    def generate_rooms(self):
        """Create and connect rooms procedurally."""
        num_rooms = 9
        boss_room = Room(800, 800, is_boss_room=True)
        rooms = [Room(600, 600) for _ in range(num_rooms)] + [boss_room]
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
