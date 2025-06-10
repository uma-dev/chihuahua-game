from screens.base_screen import BaseScreen


class MenuScreen(BaseScreen):
    def __init__(self, screen, state_manager):
        self.screen = screen
        self.state_manager = state_manager

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self):
        pass
