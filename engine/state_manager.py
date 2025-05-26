from screens.gameplay_screen import GameplayScreen


class StateManager:
    def __init__(self, screen, initial_screen=None):
        self.screen = screen
        if initial_screen:
            self.current_screen = initial_screen
        else:
            self.current_screen = GameplayScreen(screen)

    def handle_event(self, event):
        self.current_screen.handle_event(event)

    def update(self, dt):
        self.current_screen.update(dt)

    def render(self):
        self.current_screen.render()

    def change_state(self, new_screen):
        self.current_screen = new_screen(self.screen)
