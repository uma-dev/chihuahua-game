# Chihuahua Game 🐕

> A 2D Chihuahua-themed reinforcement learning environment built with Pygame and Gymnasium.

---

## 🚀 Overview

This is a 2D Pygame environment for training reinforcement learning agents. It includes:

* A custom RL environment compatible with Gymnasium
* Modular game structure using Pygame (clean architecture)
* **Object-Oriented Programming (OOP)** for organizing game logic

Check out my another work in progress project: [Car Game](https://github.com/uma-dev/car-game).

---

## 📋 Table of Contents

1. [Features](#-features)
2. [Prerequisites](#-prerequisites)
3. [Installation](#-installation)
4. [Usage](#-usage)
5. [Environment](#-game-structure)
6. [Creating Custom Levels](#-creating-custom-levels)
7. [Contributing](#-contributing)
8. [License](#-license)

---

## 🎮 Features

* Discrete Reinforcement Learning environment
* Collision-based rewards: hitting a target tile
* Partial rewards: getting the ball near to the target tile
* Frame-based animation, sprites, basic physics and level loading
* Easy to integrate with Gym-based RL pipelines
* Playable characters with simple animations (render states)

<p align="center">
  <img alt="Prerequisites: Game.py setup" src="https://user-images.githubusercontent.com/22565959/215545981-3a106e1a-6674-49c9-b493-a059da383bf4.png">
</p>

---

## 🔧 Prerequisites

* **Python 3.7+**
* uv (recommended)
* modules: pygame, gymnasium, tensorboard (see requirements.txt)

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/uma-dev/chihuahua-game.git
   cd chihuahua-game
   ```

2. (Optional) Create a virtual environment:

   ```bash
   uv venv 
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows
   ```

3. Install dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

---

## ▶️ Usage

Play the game with:

```bash
python game.py
```

Use arrow keys (← ↑ → ↓) to move your chihuahua. Enjoy!

<p align="center">
  <img
    alt="Executing Game.py"
    src="https://user-images.githubusercontent.com/22565959/215546502-d1f4a86c-70ad-4ddd-95a5-32db8f98188f.png">
</p>

---

## 🧠 Environment

* **`Game.py`**: Entry point, initializes Pygame and game loop
* **`sprites/`**: Folder containing character and environment images
* **`classes/`**: Python modules defining game entities and logic
* **`levels/`**: JSON or text files defining custom level layouts

---

## 🧠 Environment Details

Discrete Observation Space: Position and velocity of ball and character

Discrete Action Space: Move left / right / jump/ sprint / no action

Rewards:

+10 for hitting target blocks

-0.1 for every non successful step

Partial rewards based on distance to target tile:

``` python
dist < 5:
  reward += 3
elif dist < 10:
  reward += 2
elif dist < 100:
  reward += 1

```

Done Condition: Level completion or failure

Use env.render() to visualize the episode during training or testing.

---

## 🛠️ Custom Levels

Define JSON layout files in the levels/ folder

Add custom tilemaps, special blocks, or enemies

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a pull request.

---
