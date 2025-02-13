import arcade
from game.game import DimensionShiftGame

def main():
    """Start the game."""
    game = DimensionShiftGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
