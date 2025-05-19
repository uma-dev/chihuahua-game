import pygame
from entities.ball import Ball
from entities.character import Character
from utils.constants import COLORS, SIZE


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Chihuahua game")
        self.running = True
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.drawable_sprites = pygame.sprite.Group()

        self.character = Character(self.screen, (SIZE[0] / 2), SIZE[1] - 100)
        self.ball = Ball(SIZE[0] // 2, -5000)

        self.all_sprites.add(self.character, self.ball)
        self.drawable_sprites.add(self.character, self.ball)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.character.can_hit_ball(
                    self.ball
                ):
                    self.character.hit_ball(self.ball)
                self.keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.keyup(event.key)
            elif event.type == pygame.K_r:
                self.ball.reset()

    def keydown(self, event_key):
        self.character.key_down(event_key)

    def keyup(self, event_key):
        self.character.key_up(event_key)

    def update(self, dt):
        self.all_sprites.update(dt)
        self.check_character_collisions()

    def check_character_collisions(self):
        if pygame.sprite.collide_mask(self.character, self.ball):
            hit_direction = pygame.math.Vector2(
                self.ball.rect.center
            ) - pygame.math.Vector2(self.character.rect.center)
            if hit_direction.length() > 0:
                hit_direction = hit_direction.normalize()

            # Apply force based on character's movement
            force = hit_direction * 12 + pygame.math.Vector2(0, -10)
            force += pygame.math.Vector2(self.character.dx * 0.5, 0)
            self.ball.apply_force(force)

    def render(self):
        self.screen.fill(COLORS["sky_blue"])

        for sprite in self.drawable_sprites:
            sprite.draw(self.screen)

        pygame.display.flip()

    def runGame(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # seconds
            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.runGame()
