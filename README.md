# Bullet Hell Roguelike

## Overview
This is a top-down shooter game where the player must navigate procedurally generated rooms, defeat enemies, and survive as long as possible. The game features randomly generated rooms with enemy encounters and a locked-room system until all enemies are defeated.

## Room Generation Issue
Currently, the room generation system is not functioning as expected. Although the room generation logic is in place, the rooms are not being generated properly, which results in the game not displaying at all or stopping to game from even working. This issue prevents the game from showing procedurally generated environments, affecting the overall gameplay experience. The issue is being investigated, and a fix will be implemented soon to ensure that rooms are generated and displayed correctly.


## Features
- Procedurally generated rooms
- Locked rooms until enemies are defeated
- Various enemy types with unique attack patterns
- Simple movement and shooting mechanics

## Controls
- **WASD / Arrow Keys** – Move the player
- **Mouse Click** – Shoot towards the cursor

## Installation
1. Ensure you have Python installed (recommended version 3.8+).
2. Install dependencies using:
   ```sh
   pip install arcade
   ```
3. Run the game with:
   ```sh
   python game.py
   ```

## File Structure
- `game.py` – Main game loop
- `level.py` – Room and level generation
- `player.py` – Player character logic
- `enemy.py` – Enemy AI and behavior
- `bullet.py` – Bullet logic
- `floor_gen.py` – Room background and collision management

## Assets
All assets are stored in the `assets/` directory, including player and enemy sprites, as well as sound effects.

## Future Improvements
- More enemy types and attack patterns
- Enhanced room layouts and difficulty scaling

## License
This project is for educational purposes. Feel free to modify and expand upon it.