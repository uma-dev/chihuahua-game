import pygame
from map.level_loader import LevelLoader
from screens.base_screen import BaseScreen
from entities.character import Character
from entities.ball import Ball
from utils.constants import COLORS


class GameplayScreen(BaseScreen):
    def __init__(self, screen):
        self.screen = screen

        self.level = LevelLoader.load("level_01.json")
        start_x, start_y = self.level.start_pos
        ball_x, ball_y = self.level.ball_spawn
        self.character = Character(self.screen, start_x, start_y)
        self.ball = Ball(ball_x, ball_y)

        self.all_sprites = pygame.sprite.Group()
        self.drawable_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.character, self.ball)
        self.drawable_sprites.add(self.character, self.ball)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.character.can_hit_ball(self.ball):
                self.character.hit_ball(self.ball)
            self.character.key_down(event.key)

        elif event.type == pygame.KEYUP:
            self.character.key_up(event.key)

        elif event.type == pygame.K_r:
            self.ball.reset()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.check_collisions()

    def render(self):
        self.screen.fill(COLORS["sky_blue"])
        self.level.draw(self.screen)
        for sprite in self.drawable_sprites:
            sprite.draw(self.screen)
        pygame.display.flip()

    def check_collisions(self):
        if pygame.sprite.collide_mask(self.character, self.ball):
            hit_direction = pygame.math.Vector2(
                self.ball.rect.center
            ) - pygame.math.Vector2(self.character.rect.center)
            if hit_direction.length() > 0:
                hit_direction = hit_direction.normalize()

            force = hit_direction * 12 + pygame.math.Vector2(0, -10)
            force += pygame.math.Vector2(self.character.dx * 0.5, 0)
            self.ball.apply_force(force)
