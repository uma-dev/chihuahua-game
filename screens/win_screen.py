import pygame
from screens.base_screen import BaseScreen
from utils.constants import COLORS, SCREEN_HEIGHT, SCREEN_WIDTH, WIN_FONT_SIZE
from utils.game_states import GameState


class WinScreen(BaseScreen):
    def __init__(self, screen, state_manager):
        self.screen = screen
        self.state_manager = state_manager

        self.big_font = pygame.font.Font(None, WIN_FONT_SIZE)
        self.small_font = pygame.font.Font(None, WIN_FONT_SIZE // 3)

        self.big_text = self.big_font.render("Win!", True, COLORS["win_text"])
        self.small_text = self.small_font.render(
            "Press ENTER", True, COLORS["win_text"]
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.state_manager.change_state(GameState.GAMEPLAY)

    def update(self, dt):
        pass

    def render(self):
        # self.screen.fill(COLORS["sky_blue"])
        self._blit_centered(self.big_text, y_offset=-WIN_FONT_SIZE // 2)
        self._blit_centered(self.small_text, y_offset=WIN_FONT_SIZE // 2)
        pygame.display.flip()

    def _blit_centered(self, surface, y_offset=0):
        rect = surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset)
        )
        self.screen.blit(surface, rect)
