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
    ball_center = pygame.math.Vector2(ball.rect.center)
    target_center = pygame.math.Vector2(target.rect.center)
    distance = ball_center.distance_to(target_center)

    overlap = target.rect.width / 2

    return distance <= overlap
