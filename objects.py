"""
Defines all objects for the game.
"""
import pygame
import pygame.freetype

class Logo:
    """
    Defines rects for logo.
    """

    def __init__(self, settings):
        self.settings = settings

        # Logo rect settings
        logo_height = (self.settings.height * 2) // 5
        logo_width = self.settings.width // 20
        logo_x_pos = [x for x in range(self.settings.width // 6, self.settings.width - (self.settings.width // 10),
            self.settings.width // 5)]
        logo_y_final = self.settings.height // 10

        # Logo rect boards
        boards = [pygame.Rect(x, logo_y_final, logo_width, logo_height) for x in logo_x_pos]

        # Array of characters, with each character being an array of lines to render the logo
        self.logo = [
                [boards[0].bottomleft, boards[0].topleft, boards[0].topright, boards[0].midright, boards[0].midleft],
                [boards[1].topleft, boards[1].topright, boards[1].bottomright, boards[1].bottomleft,
                boards[1].topleft],
                [boards[2].bottomleft, boards[2].topleft, boards[2].bottomright, boards[2].topright],
                [boards[3].topright, boards[3].topleft, boards[3].bottomleft, boards[3].bottomright,
                boards[3].midright, boards[3].center]
                ]

class Selection:
    """
    Defines Selection Text
    """

    def __init__(self, settings):
        pygame.freetype.init()

        self.settings = settings
        self.font = pygame.freetype.Font("assets/saxmono.ttf", size=self.settings.height // 25)

        self.text = ["ONE PLAYER", "TWO PLAYER"]
        self.gap = self.settings.height // 10
        self.position = 7 * self.gap
        self.text_width = self.font.get_rect(self.text[0]).width
        self.text_height = self.font.get_rect(self.text[0]).height
        self.starting = (self.settings.width // 2) - (self.text_width // 2)

        cursor_size = self.text_height

        self.cursor = pygame.Rect(self.starting - (self.settings.width // 10), self.position,
            cursor_size, cursor_size)


"""
    def cursor(self):

        self.cursr = pygame.Rect(self.starting - (self.w // 10), self.gap * 7, self.text_height * 2, self.text_height)
        pygame.draw.rect(self.surface, self.font_color, self.cursr)
        # Font Settings
        self.font = pygame.freetype.Font("assets/saxmono.ttf", size = self.h // 25)
        self.font_color = (255, 255, 255)
        self.message = ["ONE PLAYER", "TWO PLAYER"]   
"""