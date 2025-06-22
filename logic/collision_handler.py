import pygame
import pygame.math


def character_hits_ball(character, ball):
    if pygame.sprite.collide_mask(character, ball):
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(
            character.rect.center
        )
        if direction.length() > 0:
            direction = direction.normalize()
        force = direction * 12 + pygame.math.Vector2(0, -10)
        force += pygame.math.Vector2(character.dx * 0.5, 0)
        ball.apply_force(force)


def ball_hits_target(ball, target):
    return pygame.sprite.collide_rect(ball, target)
