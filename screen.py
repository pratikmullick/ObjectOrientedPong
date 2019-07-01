import pygame

class Display:
    """
    Renders objects to screen.
    """

    def __init__(self, settings):
        pygame.init()
        pygame.display.set_caption("TEST")
        self.settings = settings
        self.surface = pygame.display.set_mode((self.settings.width, self.settings.height), 0, 8)
        self.surface.fill((0,0,0))
        pygame.display.update()

class GameScreen(Display):
    """
    Renders the game screen to the Display (parent) class.
    """

    def __init__(self, settings):
        super().__init__(settings)
