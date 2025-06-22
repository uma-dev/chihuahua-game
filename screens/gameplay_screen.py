import pygame
from entities.target import Target
from logic.collision_handler import ball_hits_target, character_hits_ball
from map.level_loader import LevelLoader
from screens.base_screen import BaseScreen
from entities.character import Character
from entities.ball import Ball
from utils.constants import COLORS
from utils.game_states import GameState


class GameplayScreen(BaseScreen):
    def __init__(self, screen, state_manager):
        self.screen = screen
        self.state_manager = state_manager
        self.level = LevelLoader.load("level_01.json")

        start_x, start_y = self.level.start_pos
        ball_x, ball_y = self.level.ball_spawn
        target_x, target_y = self.level.target

        self.character = Character(self.screen, start_x, start_y)
        self.ball = Ball(ball_x, ball_y)
        self.target = Target(target_x, target_y)

        self.all_sprites = pygame.sprite.Group()
        self.drawable_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.character, self.ball, self.target)
        self.drawable_sprites.add(self.character, self.ball, self.target)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.character.can_hit_ball(self.ball):
                self.character.hit_ball(self.ball)

            self.character.key_down(event.key)

        elif event.type == pygame.KEYUP:
            self.character.key_up(event.key)

    def update(self, dt):
        self.all_sprites.update(dt)
        character_hits_ball(self.character, self.ball)

        if ball_hits_target(self.ball, self.target):
            print("Win!")
            self.state_manager.change_state(GameState.WIN)

    def render(self):
        self.screen.fill(COLORS["sky_blue"])
        self.level.draw(self.screen)
        for sprite in self.drawable_sprites:
            sprite.draw(self.screen)
        pygame.display.flip()
