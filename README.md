# Dimension Shift: Bullet Hell Roguelike

## About the Game
**Dimension Shift** is a bullet hell roguelike where players traverse alternate dimensions, facing random bosses and challenging bullet patterns. The game is developed in **Python** using the **Arcade** library.

---

## Setting Up the Environment

### 1. Clone the Repository
Before starting, make sure to clone the repository:

```bash
  git clone https://github.com/wesgtr/bullet-hell-roguelike
  cd dimension-shift
``` 

### 2. Create and Activate a Virtual Environment (venv)
To keep dependencies organized, use a virtual environment:
```bash
  python -m venv venv
```

activate the virtual environment
```bash
  venv\Scripts\activate
```

### 3. Install Dependencies
Now, install the required libraries:

```bash
  pip install -r requirements.txt
```
If you need to add new dependencies during development, use:
```bash
  pip freeze > requirements.txt
```

### 4. Running the Game
After setting up the environment, run the following command to start the game:

```bash
  python main.py
```

To deactivate the virtual environment, use:

```bash
  deactivate
```