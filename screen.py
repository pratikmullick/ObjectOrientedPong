import pygame
import pygame.freetype
from options import Configuration       # For Debug Purposes Only
import sys                              # For Debug Purposes Only

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
    Generates opening screen to the Display (parent class).
    """

    def __init__(self, settings):
        super().__init__(settings)
        pygame.freetype.init()

        # Shortening for easier typing
        self.w = self.settings.width
        self.h = self.settings.height

        # Font Settings
        self.font = pygame.freetype.Font("assets/saxmono.ttf", size = self.h // 25)
        self.font_color = (255, 255, 255)
        self.message = ["ONE PLAYER", "TWO PLAYER"]   

        # Automatically run function when class is initialized
        self.fps_clock = pygame.time.Clock()
        self.render_logo()
        self.player_selection()
        self.cursor()
        pygame.display.update()
        self.fps_clock.tick(self.settings.fps)

    def render_logo(self):
        """
        Renders vectorized logo.
        """
        logo_height = (self.h * 2) // 5
        logo_width = self.w // 20
        logo_color = (255, 255, 255)
        logo_line = self.w // 50
        
        logo_x_pos = [x for x in range(self.w // 6, self.w - (self.w // 10), self.w // 5)]
        logo_y_init = self.h + (self.h // 10)
        logo_y_final = self.h // 10

        # Array of Rects to hold logo characters in place
        boards = [pygame.Rect(x, logo_y_final, logo_width, logo_height) for x in logo_x_pos]

        # Array of characters, with each character being an array of lines to render the logo
        logo = [    
                [boards[0].bottomleft, boards[0].topleft, boards[0].topright, boards[0].midright, boards[0].midleft],
                [boards[1].topleft, boards[1].topright, boards[1].bottomright, boards[1].bottomleft,
                 boards[1].topleft],
                [boards[2].bottomleft, boards[2].topleft, boards[2].bottomright, boards[2].topright],
                [boards[3].topright, boards[3].topleft, boards[3].bottomleft, boards[3].bottomright,
                 boards[3].midright, boards[3].center]
               ]


        for logo_chr in range(4):
            pygame.draw.lines(self.surface, logo_color, False, logo[logo_chr], logo_line)

    def player_selection(self):
        """
        Renders player selection menu.
        """
        self.gap = self.h // 10
        self.height = 7 * self.gap

        for player in self.message:
            self.text_width = self.font.get_rect(player).width
            self.starting = (self.w // 2) - (self.text_width // 2)
            self.text_height = self.font.get_rect(player).height
            self.font.render_to(self.surface, (self.starting, self.height), player, fgcolor=self.font_color)
            self.height += self.gap

    def cursor(self):

        board = pygame.Rect(self.starting - (self.w // 10), self.gap * 7, self.text_height * 2, self.text_height)
        cursor = [board.midtop, board.midright, board.midleft, board.midright, board.midbottom]
        pygame.draw.lines(self.surface, self.font_color, False, cursor, self.w // 250)


class GameScreen(Display):
    """
    Renders the game screen to the Display (parent) class.
    """

    def __init__(self, settings):
        super().__init__(settings)

# Debug
if __name__ == "__main__":
    confy = Configuration(".pong.conf")
    Display(confy)
    # OpeningScreen(confy)

    while True:
        for event in pygame.event.get():
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif key[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif key[pygame.K_RETURN]:
                active = True

    if active:
        print("Changing to Game Screen")

