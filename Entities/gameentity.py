from pygame import sprite


class GameEntity(sprite.Sprite):
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

    def draw(self, surface):
        self.display.blit(self.image, self.rect)
