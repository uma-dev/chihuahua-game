import pygame

from utils.constants import COLORS, TARGET_SIZE


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TARGET_SIZE, TARGET_SIZE), pygame.SRCALPHA)
        self._draw_ring()
        self.rect = self.image.get_rect(topleft=(x, y))

    def _draw_ring(self):
        center = (TARGET_SIZE // 2, TARGET_SIZE // 2)
        radius = TARGET_SIZE // 2
        thickness = 4
        pygame.draw.circle(self.image, COLORS["target"], center, radius, thickness)

    def draw(self, surface):
        """Draw the ball to the specified surface"""
        surface.blit(self.image, self.rect)
