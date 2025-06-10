from screens.gameplay_screen import GameplayScreen
from screens.menu_screen import MenuScreen
from screens.win_screen import WinScreen
from utils.game_states import GameState


class StateManager:
    def __init__(self, screen):
        self.screen = screen
        self.factories = {
            GameState.GAMEPLAY: lambda: GameplayScreen(self.screen, self),
            GameState.WIN: lambda: WinScreen(self.screen, self),
            GameState.MENU: lambda: MenuScreen(self.screen, self),
        }
        self.current_screen = GameplayScreen(screen, self)

    def handle_event(self, event):
        self.current_screen.handle_event(event)

    def update(self, dt):
        self.current_screen.update(dt)

    def render(self):
        self.current_screen.render()

    def change_state(self, new_state: GameState):
        if new_state in self.factories:
            self.current_screen = self.factories[new_state]()
        else:
            raise ValueError(f"No screen registered for state: {new_state}")
