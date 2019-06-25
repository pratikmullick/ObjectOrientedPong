import pygame, sys
from options import Configuration       # For Debug Purposes Only

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

class OpeningScreen(Display):
    """
    Generates opening screen.
    """

    def __init__(self, settings):
        super().__init__(settings)
        self.logo_height = (self.settings.height * 2) // 5
        self.logo_width = self.settings.width // 20
        self.color = (192, 192, 192)
        self.line = self.settings.width // 50

        # For code shortening (explicitly visual)
        w = self.settings.width

        self.logo_x_pos = [x for x in range(w // 6, w - (w // 10), w // 5)]
        self.logo_y_init = self.settings.height + (self.settings.height // 10)
        self.logo_y_final = self.settings.height // 10

        self.boards = [pygame.Rect(x, self.logo_y_final, self.logo_width, self.logo_height) for x in self.logo_x_pos]

        self.logo = [
                        [
                            self.boards[0].bottomleft, self.boards[0].topleft, self.boards[0].topright,
                            self.boards[0].midright, self.boards[0].midleft
                        ],
                        [
                            self.boards[1].topleft, self.boards[1].topright, self.boards[1].bottomright,
                            self.boards[1].bottomleft, self.boards[1].topleft
                        ],
                        [
                            self.boards[2].bottomleft, self.boards[2].topleft, self.boards[2].bottomright,
                            self.boards[2].topright
                        ],
                        [
                            self.boards[3].topright, self.boards[3].topleft, self.boards[3].bottomleft,
                            self.boards[3].bottomright,self.boards[3].midright, self.boards[3].center
                        ]
                    ]

    def render_logo(self):
        fps_clock = pygame.time.Clock()
        for logo_chr in range(4):
            pygame.draw.lines(self.surface, self.color, False, self.logo[logo_chr], self.line)
        pygame.display.update()
        fps_clock.tick(self.settings.fps)


# Debug
if __name__ == "__main__":
    confile = ".pong.conf"
    ops = OpeningScreen(Configuration(confile))

    while True:
        ops.render_logo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

