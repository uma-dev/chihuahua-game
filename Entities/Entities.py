import pygame
from Utils.States import AnimatedState, StaticState


class GameEntity(pygame.sprite.Sprite):
    def __init__(self, display):
        super(GameEntity, self).__init__()
        self.display = display
        self.states_dict = {}
        self.current_state = None
        self.dx = 0
        self.dy = 0
        self.image = None
        self.rect = None
        self.jumping = False

    def set_current_state(self, key):
        self.current_state = self.states_dict[key]
        self.image = self.current_state.get_sprite()

        if self.rect is not None:
            old_pos = self.rect.topleft
            self.rect = self.image.get_rect()
            self.rect.topleft = old_pos

    def impulse(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def update(self, dt):
        raise NotImplementedError("The update method must be called in any child class")

    def draw(self):
        self.display.blit(self.image, self.rect)


class Character(GameEntity):
    def __init__(self, display, px, py):
        super(Character, self).__init__(display)  # new window
        self.speed = 2.5
        self.walking_images = pygame.image.load("assets/images/almendra.png")
        self.number_of_sprites = 4
        self.walking_right_state = AnimatedState(
            self.walking_images.subsurface(
                0,
                0,
                self.walking_images.get_width(),
                self.walking_images.get_height() / 2,
            ),
            self.number_of_sprites,
            400,
            "walking_right",
        )
        self.walking_left_state = AnimatedState(
            self.walking_images.subsurface(
                0,
                self.walking_images.get_height() / 2,
                self.walking_images.get_width(),
                self.walking_images.get_height() / 2,
            ),
            self.number_of_sprites,
            400,
            "walking_left",
        )
        self.resting_left_state = StaticState(
            self.walking_images.subsurface(
                self.walking_images.get_width() * 3 / 4,
                self.walking_images.get_height() / 2,
                self.walking_images.get_width() / self.number_of_sprites,
                self.walking_images.get_height() / 2,
            ),
            "resting_left",
        )
        self.resting_right_state = StaticState(
            self.walking_images.subsurface(
                0,
                0,
                self.walking_images.get_width() / self.number_of_sprites,
                self.walking_images.get_height() / 2,
            ),
            "resting_right",
        )
        self.states_dict["walking_right"] = self.walking_right_state
        self.states_dict["walking_left"] = self.walking_left_state
        self.states_dict["resting_left"] = self.resting_left_state
        self.states_dict["resting_right"] = self.resting_right_state

        self.set_current_state("resting_left")
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

        self.accelerating = False
        self.jumping = False

    def calculate_gravity(self):
        if self.dy != 0:
            self.dy = self.dy + 0.55
        else:
            self.dy = 1

    def jump(self, jump_force):
        self.impulse(self.dx, -jump_force)

    def key_down(self, key):
        if key == pygame.K_UP:
            if not self.jumping:
                self.jump(12)
                self.jumping = True
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_LEFT:
            self.set_current_state("walking_left")
            self.dx = -self.speed
        if key == pygame.K_RIGHT:
            self.set_current_state("walking_right")
            self.dx = self.speed
        if key == pygame.K_LSHIFT:
            self.speed = self.speed * 5

    def key_up(self, key):
        if key == pygame.K_UP:
            pass
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_LEFT:
            if self.dx < 0:
                self.set_current_state("resting_left")
                self.dx = 0
        if key == pygame.K_RIGHT:
            if self.dx > 0:
                self.set_current_state("resting_right")
                self.dx = 0
        if key == pygame.K_LSHIFT:
            self.speed = 2.5  # restore initial value

    def update(self, dt):
        self.calculate_gravity()

        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy

        # Boundaries
        screen_width = self.display.get_width()
        screen_height = self.display.get_height()

        if self.rect.left < 0:
            self.rect.left = 0
            self.set_current_state("resting_left")
            self.dx = 0

        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.set_current_state("resting_right")
            self.dx = 0

        if self.rect.bottom > screen_height:
            self.rect.y = self.display.get_height() - self.rect.height
            self.jumping = False
            self.dy = 0

        if self.current_state is None:
            raise RuntimeError("current_state must be set before update()")

        self.current_state.update(dt)
        self.image = self.current_state.get_sprite()
