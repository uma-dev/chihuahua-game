import pygame
from engine.state_manager import StateManager
from utils.constants import CAPTION, SIZE


class GameEngine:
    def __init__(self, initial_screen=None):
        """
        Core game engine that runs the main loop and delegates
        events, updates, and rendering to the StateManager.

        :param initial_screen: Optional Screen class to start with
        """
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_manager = StateManager(self.screen)

    def run(self):
        """
        Starts the main loop: handle events, update current state,
        render, and cap the frame rate at 60 FPS.
        """
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.state_manager.handle_event(event)

            self.state_manager.update(dt)
            self.state_manager.render()

        pygame.quit()
