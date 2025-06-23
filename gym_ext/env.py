import numpy as np
import pygame
import gymnasium as gym
from gymnasium import spaces
from logic.collision_handler import ball_hits_target, character_hits_ball
from map.level_loader import LevelLoader
from entities.character import Character
from entities.ball import Ball
from entities.target import Target
from utils.constants import (
    CHARACTER_SPRINT_SPEED,
    COLORS,
    SCREEN_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class ChihuahuaEnv(gym.Env):
    """
    Gymnasium environment wrapping the Pygame-based Chihuahua game.
    Action space:
        0: No-op, 1: Left, 2: Right, 3: Jump, 4: Sprint
    Observation:
        [char_x, char_y, char_vx, char_vy,
         ball_x, ball_y, ball_vx, ball_vy,
    """

    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(self, render_mode="human"):
        super().__init__()
        self.render_mode = render_mode

        # Action spaces
        self.action_space = spaces.Discrete(5)

        # Observation spaces
        low = np.array(
            [0, 0, -CHARACTER_SPRINT_SPEED, -CHARACTER_SPRINT_SPEED] * 2,
            dtype=np.float32,
        )
        high = np.array(
            [
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                CHARACTER_SPRINT_SPEED,
                CHARACTER_SPRINT_SPEED,
            ]
            * 2,
            dtype=np.float32,
        )
        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        if render_mode == "human":
            pygame.init()
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
        else:
            self.screen = pygame.Surface(SCREEN_SIZE)

        self.level = LevelLoader.load("level_01.json")
        self.clock = pygame.time.Clock()

        start_x, start_y = self.level.start_pos
        ball_x, ball_y = self.level.ball_spawn
        target_x, target_y = self.level.target

        self.character = Character(self.screen, start_x, start_y)
        self.ball = Ball(ball_x, ball_y)
        self.target = Target(target_x, target_y)

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.character.reset()
        self.ball.reset()
        obs = self._get_observation()
        return obs, {}

    def step(self, action):
        # if hasattr(self.character, "clear_inputs"):
        #     self.character.clear_inputs()

        if action == 1:  # Left
            self.character.key_down(pygame.K_LEFT)
        elif action == 2:  # Right
            self.character.key_down(pygame.K_RIGHT)
        elif action == 3:  # Jump
            self.character.key_down(pygame.K_UP)
        elif action == 4:  # Sprint
            self.character.key_down(pygame.K_LSHIFT)
        # 0: No-op

        # Game physics
        dt = self.clock.tick(self.metadata["render_fps"]) / 1000.0
        self.character.update(dt)
        self.ball.update(dt)
        character_hits_ball(self.character, self.ball)

        # Reward
        reward = -0.1
        done = False

        if ball_hits_target(self.ball, self.target):  # win condition
            reward += 10
            done = True
        else:
            ball_pos = np.array([self.ball.rect.x, self.ball.rect.y])
            tgt_pos = np.array([self.target.rect.x, self.target.rect.y])
            dist = np.linalg.norm(ball_pos - tgt_pos)
            if dist < 5:
                reward += 3
            elif dist < 10:
                reward += 2
            elif dist < 100:
                reward += 1

        obs = self._get_observation()
        info = {}

        if self.render_mode == "human":
            self.render()

        return obs, reward, done, False, info

    def _get_observation(self):
        return np.array(
            [
                self.character.rect.x,
                self.character.rect.y,
                self.character.dx,
                self.character.dy,
                self.ball.rect.x,
                self.ball.rect.y,
                self.ball.velocity[0],
                self.ball.velocity[1],
            ],
            dtype=np.float32,
        )

    def render(self):
        self.screen.fill(COLORS["sky_blue"])
        self.level.draw(self.screen)
        for ent in (self.character, self.ball, self.target):
            ent.draw(self.screen)
        pygame.display.flip()

    def close(self):
        pygame.quit()
