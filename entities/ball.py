import pygame
from utils.constants import (
    COLORS,
    GRAVITY,
    BOUNCE_DAMPING,
    FRICTION,
    BALL_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._create_visual()
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = GRAVITY
        self.bounce_damping = BOUNCE_DAMPING
        self.friction = FRICTION
        self.on_ground = False
        self.air_resistance = 0.99
        self.max_speed = 20

    def _create_visual(self):
        """Create ball surface with optional trail effect"""
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            COLORS["violet"],
            (BALL_SIZE // 2, BALL_SIZE // 2),
            BALL_SIZE // 2,
        )
        pygame.draw.circle(self.image, COLORS["violet_light"], (12, 12), 6)

    def update(self, dt):
        """Update ball physics and position"""
        self._apply_physics(dt)
        self._check_boundaries()
        self._limit_speed()

    def _apply_physics(self, dt):
        """Handle all physics calculations"""
        # Apply gravity if not on ground
        if not self.on_ground:
            self.velocity.y += self.gravity * dt * 60

        # Apply air resistance
        self.velocity.x *= self.air_resistance

        # Apply ground friction
        if self.on_ground:
            self.velocity.x *= self.friction

        # Update position
        self.rect.x += self.velocity.x * dt * 60
        self.rect.y += self.velocity.y * dt * 60

    def _check_boundaries(self):
        """Handle screen boundary collisions"""
        # Horizontal boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x *= -self.bounce_damping
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x *= -self.bounce_damping

        # Vertical boundaries
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y *= -self.bounce_damping

        # Floor collision
        self.on_ground = False
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity.y *= -self.bounce_damping
            self.velocity.x *= 0.9  # Extra friction on ground hit
            self.on_ground = True

    def _limit_speed(self):
        """Prevent unrealistic speeds"""
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

    def apply_force(self, force_vector):
        """Apply external force to the ball"""
        self.velocity += force_vector

    def reset(self, x=None, y=None):
        """Reset ball to specified position or center"""
        x = SCREEN_WIDTH // 2
        y = y if y is not None else SCREEN_HEIGHT // 2
        self.rect.center = (x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def draw(self, surface):
        """Draw the ball to the specified surface"""
        surface.blit(self.image, self.rect)
