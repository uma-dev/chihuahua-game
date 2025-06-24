import pygame
from .gameentity import GameEntity
from utils.States import AnimatedState, StaticState
from utils.constants import (
    CHARACTER_JUMP_FORCE,
    CHARACTER_SPEED,
    CHARACTER_SPRINT_SPEED,
    SCREEN_WIDTH,
)


class Character(GameEntity):
    """
    Player-controlled character with walking, resting, jumping, and ball-hitting capabilities.
    """

    SPRITE_PATH = "assets/images/almendra.png"
    FRAME_COUNT = 4
    FRAME_DURATION_MS = 400

    def __init__(self, display, x: int, y: int):
        super().__init__(display)
        self.speed = CHARACTER_SPEED
        self._load_sprites()
        self._init_states()

        self.set_current_state("resting_left")
        self.start_x = SCREEN_WIDTH // 2
        self.start_y = y
        self.rect = self.image.get_rect(topleft=(x, y))

        self.accelerating = False
        self.jumping = False
        self.sprinting = False

    def _load_sprites(self):
        sheet = pygame.image.load(self.SPRITE_PATH)
        total_w, total_h = sheet.get_size()
        half_h = total_h // 2
        frame_w = total_w // self.FRAME_COUNT

        # Rows: 0 = top (walk right/rest right), 1 = bottom (walk left/rest left)
        self.rows = {
            "right": sheet.subsurface((0, 0, total_w, half_h)),
            "left": sheet.subsurface((0, half_h, total_w, half_h)),
        }
        self.frame_size = (frame_w, half_h)

    def _init_states(self):
        self.walking_right = AnimatedState(
            self.rows["right"],
            self.FRAME_COUNT,
            self.FRAME_DURATION_MS,
            "walking_right",
        )
        self.walking_left = AnimatedState(
            self.rows["left"], self.FRAME_COUNT, self.FRAME_DURATION_MS, "walking_left"
        )

        # Resting (static) frames: first frame of right, last frame of left
        frame_w, frame_h = self.frame_size
        right_rest = self.rows["right"].subsurface(0, 0, frame_w, frame_h)
        left_rest = self.rows["left"].subsurface(
            frame_w * (self.FRAME_COUNT - 1), 0, frame_w, frame_h
        )

        self.resting_right = StaticState(right_rest, "resting_right")
        self.resting_left = StaticState(left_rest, "resting_left")

        # Register states
        for state in (
            self.walking_right,
            self.walking_left,
            self.resting_right,
            self.resting_left,
        ):
            self.states_dict[state.name] = state

    def calculate_gravity(self):
        # simple gravity: accelerate down
        self.dy = min(self.dy + 0.55, 10.0)

    def jump(self, force: float = 12):
        if not self.jumping:
            self.impulse(self.dx, -force)
            self.jumping = True

    def key_down(self, key):
        if key == pygame.K_UP:
            self.jump(CHARACTER_JUMP_FORCE)
        elif key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPRINT_SPEED if self.sprinting else -CHARACTER_SPEED
            self.set_current_state("walking_left")
        elif key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPRINT_SPEED if self.sprinting else CHARACTER_SPEED
            self.set_current_state("walking_right")
        elif key == pygame.K_LSHIFT:
            self.sprinting = True
            # Update dx if already moving
            if self.dx > 0:
                self.dx = CHARACTER_SPRINT_SPEED
            elif self.dx < 0:
                self.dx = -CHARACTER_SPRINT_SPEED

    def key_up(self, key):
        if key in (pygame.K_LEFT, pygame.K_RIGHT):
            if (key == pygame.K_LEFT and self.dx < 0) or (
                key == pygame.K_RIGHT and self.dx > 0
            ):
                side = "left" if key == pygame.K_LEFT else "right"
                self.set_current_state(f"resting_{side}")
                self.dx = 0
        elif key == pygame.K_LSHIFT:
            self.sprinting = False
            # Update dx if already moving
            if self.dx > 0:
                self.dx = CHARACTER_SPEED
            elif self.dx < 0:
                self.dx = -CHARACTER_SPEED

    def update(self, dt: float):
        self.calculate_gravity()
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Keep inside screen
        w, h = self.display.get_size()
        if self.rect.left < 0:
            self._clamp_x(0, "resting_left")
        if self.rect.right > w:
            self._clamp_x(w - self.rect.width, "resting_right")
        if self.rect.bottom > h:
            self.rect.bottom = h
            self.jumping = False
            self.dy = 0

        if self.current_state is None:
            raise RuntimeError("No current state set")

        # Advance animation and update sprite
        self.current_state.update(dt * 1000)
        self.image = self.current_state.get_sprite()

    def _clamp_x(self, new_x: int, rest_state: str):
        self.rect.x = new_x
        self.dx = 0
        self.set_current_state(rest_state)

    def hit_ball(self, ball):
        dir_vec = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(
            self.rect.center
        )
        if dir_vec.length() > 0:
            dir_vec.normalize_ip()
        force = dir_vec * 12 + pygame.math.Vector2(0, -10)
        ball.apply_force(force)

    def can_hit_ball(self, ball) -> bool:
        dx = abs(self.rect.centerx - ball.rect.centerx)
        dy = ball.rect.bottom - self.rect.top
        return dy < 50 and dx < 100

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.dx = 0
        self.dy = 0
        self.jumping = False
        self.sprinting = False
