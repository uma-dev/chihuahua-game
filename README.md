# Chihuahua Game 🐕

> A 2D Chihuahua-themed game built using OOP principles and Pygame in Python. A beginner-friendly introduction to object-oriented programming through game development.

---

## 🚀 Overview

This is a work-in-progress 2D game featuring chihuahua dogs. It demonstrates the use of:

* **Object-Oriented Programming (OOP)** for organizing game logic
* **Pygame** for rendering graphics and handling input
* **Python** as the development language

Check out another example project: [Car Game](https://github.com/uma-dev/car-game).

---

## 📋 Table of Contents

1. [Features](#-features)
2. [Prerequisites](#-prerequisites)
3. [Installation](#-installation)
4. [Usage](#-usage)
5. [Game Structure](#-game-structure)
6. [Creating Custom Levels](#-creating-custom-levels)
7. [Adding New Characters](#-adding-new-characters)
8. [Contributing](#-contributing)
9. [License](#-license)

---

## 🎮 Features

* Playable chihuahua characters with simple animations
* Keyboard controls for movement and actions
* Easily extendable via classes for new levels and characters
* Demonstrates sprite handling, collision detection, and game loops

---

## 🔧 Prerequisites

Ensure you have the following installed:

* **Python 3.7+**
* **Pygame** module

<p align="center">
  <img alt="Prerequisites: Game.py setup" src="https://user-images.githubusercontent.com/22565959/215545981-3a106e1a-6674-49c9-b493-a059da383bf4.png">
</p>

### Helpful Links

* **Install Python**

  * Windows: [https://learn.microsoft.com/en-us/windows/python/beginners](https://learn.microsoft.com/en-us/windows/python/beginners)
  * Linux: [https://docs.python-guide.org/starting/install3/linux/](https://docs.python-guide.org/starting/install3/linux/)
* **Install Pip**: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)
* **Pygame Guide**: [https://www.pygame.org/wiki/GettingStarted](https://www.pygame.org/wiki/GettingStarted)

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/uma-dev/chihuahua-game.git
   cd chihuahua-game
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the game with:

```bash
python Game.py
```

Use arrow keys (← ↑ → ↓) to move your chihuahua. Enjoy!

<p align="center">
  <img alt="Executing Game.py" src="https://user-images.githubusercontent.com/22565959/215546502-d1f4a86c-70ad-4ddd-95a5-32db8f98188f.png">
</p>

---

## 🏗️ Game Structure

* **`Game.py`**: Entry point, initializes Pygame and game loop
* **`sprites/`**: Folder containing character and environment images
* **`classes/`**: Python modules defining game entities and logic
* **`levels/`**: JSON or text files defining custom level layouts

### Animation Principle

Each sprite sheet is divided into frames. The game crops the appropriate sub-image each tick based on player input to animate movement.

<p align="center">
  <img alt="Canvas animation principle" src="https://user-images.githubusercontent.com/22565959/216153341-489e8766-e9f3-4882-bef6-65a41cce2931.png">
</p>

---

## 📝 Class diagram

1. Open the class diagram (`Classes of game.dia`) for an overview of object relationships.

<p align="center">
  <img alt="Class diagram" src="https://user-images.githubusercontent.com/22565959/215545446-4c557d95-b2c1-4878-96be-ac669e9e4e3f.png">
</p>

2. Define a new level file in `levels/` following the existing format.
3. Load your level in `Game.py` by specifying its path.

> **Tip:** Install [Dia](http://dia-installer.de/) to view `.dia` files. On Linux:

 ```bash
 sudo apt install dia
 ```

---

## 🎨 Adding New Characters

1. Create a new sprite sheet in `assets/images/` with consistent frame sizes.
2. Add a corresponding class in `classes/` inheriting from the base `Character` class.
3. Update the character selection menu in `Game.py` to include your new sprite.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a pull request.

---