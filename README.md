# Chihuahua Game 🐕

> A 2D Chihuahua-themed reinforcement learning environment built with Pygame and Gymnasium.

---

## 🚀 Overview

2D Pygame game and environment for reinforcement learning. It includes:

* A custom RL environment compatible with Gymnasium
* Modular game structure using Pygame (clean architecture)
* **Object-Oriented Programming (OOP)** for organizing game logic

Check out my another work in progress project: [Car Game](https://github.com/uma-dev/car-game).

---

## 📋 Table of Contents

1. [Features](#-features)
2. [Prerequisites](#-prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [RL Setup](#-rl-setup)
6. [Creating Custom Levels](#custom-levels)
7. [Contributing](#-contributing)

---

## 🎮 Features

* Discrete Reinforcement Learning environment
* Collision-based rewards: hitting a target tile
* Partial rewards: getting the ball near to the target tile
* Frame-based animation, sprites, basic physics and level loading
* Easy to integrate with Gym-based RL pipelines
* Playable characters with simple animations (render states)

<p align="center">
  <img alt="Digitalization" src="https://github.com/user-attachments/assets/4cbf36be-3d27-47a0-a164-aeee6a9abd8a">
</p>

### Project structure

The project is organized into modular components, separating game logic, assets, environment definitions, and training scripts:

``` bash
├── assets/              # Game assets (sprites, tiles)
│   └── images/          # Character and tile images
│       └── tiles/       # Grass, wall, and ring textures

├── engine/              # Core game engine and state manager
│   └── game_engine.py   # Game loop and scene handling

├── entities/            # Game entities like the character, ball, and target

├── gym_ext/             # Gym-compatible environment and training script
│   ├── env.py           # Gymnasium environment wrapper
│   └── train.py         # PPO or other RL agent training logic

├── logic/               # Game physics and collision handling

├── logs/                # TensorBoard logs for training visualization

├── map/                 # Level definitions (JSON) and level loader

├── models/              # (Optional) Trained models can be saved here

├── screens/             # UI screens (menu, gameplay, win state)

└── utils/               # Constants, game states, shared helpers
```

---

## 🔧 Prerequisites

* **Python 3.7+**
* uv (recommended)
* modules: pygame, gymnasium, tensorboard (see requirements.txt)

---

<a name="installation"></a>

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

<a name="usage"></a>

## ▶️ Usage

Play the game with: (Use arrow keys (← ↑ → ↓) to move your chihuahua. Enjoy!)

```bash
python game.py
```

Train the model with:

```bash
python main.py train 
```

Eval the policy with:

```bash
python main.py eval
```

Look training in real time with:

```bash
 tensorboard --logdir .\logs\ppo_tensorboard\
```

---

## 🧠 RL Setup

### Description and goal

Chihuahua 2D videogame where the agent controls a chihuahua character that must hit and push a ball toward a target tile. The environment is built with Pygame and wrapped using Gymnasium API, so its compatible with RL algorithms.

The agent's objective is to learn how to move and act efficiently to guide the ball to the target, maximizing the reward and minimizing steps (penalty).


<p align="center">
  <img
    alt="Executing Game.py"
    src="https://github.com/user-attachments/assets/fad08b8e-f179-4974-bcd4-360608192ee5">
</p>

### Problem Formulation

**State Space (Observation):**
A vector of 8 values:

```python
[char_x, char_y, char_vx, char_vy, ball_x, ball_y, ball_vx, ball_vy]
```

**Action Space:**
Discrete(5):

```python
0 = No-op, 1 = Left, 2 = Right, 3 = Jump, 4 = Sprint
```

**Reward Function:**

```python
reward = -0.1  # penalty per step
if dist < 100:
    reward += 1
if dist < 10:
    reward += 2
if dist < 5:
    reward += 3
if ball_hits_target:
    reward += 10
    done = True
```

**Learning Progress**

Here is the total reward per episode over time:

---

<a name="custom-levels"></a>

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
