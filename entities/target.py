import pygame

from utils.constants import COLORS, TARGET_SIZE


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TARGET_SIZE, TARGET_SIZE))
        self.image.fill(COLORS["target"])
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        """Draw the ball to the specified surface"""
        surface.blit(self.image, self.rect)
