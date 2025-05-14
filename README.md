# Chihuahua Game (Work in progress)

Chihuahua dogs game using [pygame](https://www.pygame.org/news) modules on **Python**.
This is a intermediate look into 2D games and a easy **introduction to OOP programming** for those who like games.
Checkout my other example [car-game](https://github.com/uma-dev/car-game) with pygame and have fun.

## How to use

### What you need

This program only needs a computer with **python** and **pygame** installed, If you don't know how to do it, here are some examples that may help.

<p align="center">
 <img alt="Game.py" src="https://user-images.githubusercontent.com/22565959/215545981-3a106e1a-6674-49c9-b493-a059da383bf4.png">
</p>

- Python
  - [Installing Python on Windows](https://learn.microsoft.com/en-us/windows/python/beginners)
  - [Installing Python on Linux](https://docs.python-guide.org/starting/install3/linux/)
- Pip
  - [Pip Installation](https://pip.pypa.io/en/stable/installation/)
- Pygame
  - [Getting started with Pygame](https://www.pygame.org/wiki/GettingStarted)

### Executing

As easy as it is, if you have not executed any python script before, take a look to the following tutorial:

- [Execute Python scripts](https://pythonbasics.org/execute-python-scripts/)
- After going to the `root` folder of the project type

```
python3 Game.py
```

<p align="center">
 <img alt="Game.py" src="https://user-images.githubusercontent.com/22565959/215546502-d1f4a86c-70ad-4ddd-95a5-32db8f98188f.png">
</p>

## Develop your own levels

You can check the file "Classes of game.dia" to take a look on the _Class diagrams_ without looking at the source code.
If you dont have already Dia installed try:

-     ``` sudo apt install dia ``` on Linux
- visit [Dia website](http://dia-installer.de/) on any platform

<p align="center">
 <img alt="Class diagram" src="https://user-images.githubusercontent.com/22565959/215545446-4c557d95-b2c1-4878-96be-ac669e9e4e3f.png">
</p>

### Animation working principle

The general idea is to make a frame with a cropped sub-image of the general canvas, the sub-image that is going to be shown on the screen depends on the command from the keyboard.

<p align="center">
 <img alt="Canvas" src="https://user-images.githubusercontent.com/22565959/216153341-489e8766-e9f3-4882-bef6-65a41cce2931.png">
</p>

### Adding a new character

As simple as making your own character canvas to generate the necesary frames with pygame, you can load a menu an select the character that you want.

### Make it executable

- Windows
- Linux
