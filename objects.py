"""
Defines all objects for the game.
"""
import time
import random
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
        logo_x_pos = [x for x in range(self.settings.width // 6, self.settings.width - (self.settings.width // 10), \
            self.settings.width // 5)]
        logo_y_final = self.settings.height // 10

        # Logo rect boards
        boards = [pygame.Rect(x, logo_y_final, logo_width, logo_height) for x in logo_x_pos]

        # Array of characters, with each character being an array of lines to render the logo
        self.logo = [
            [boards[0].bottomleft, boards[0].topleft, boards[0].topright, boards[0].midright, boards[0].midleft], \
            [boards[1].topleft, boards[1].topright, boards[1].bottomright, boards[1].bottomleft, boards[1].topleft], \
            [boards[2].bottomleft, boards[2].topleft, boards[2].bottomright, boards[2].topright], \
            [boards[3].topright, boards[3].topleft, boards[3].bottomleft, boards[3].bottomright, \
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
        self.cursor = pygame.Rect(self.starting - (self.settings.width // 10), \
            self.position, cursor_size, cursor_size)

class Borders:
    """
    Defines Game Borders, and a dashed center line.
    """

    def __init__(self, settings):
        self.settings = settings
        self.top_border = pygame.Rect((0, 0), (self.settings.width, self.settings.line))
        self.bottom_border = pygame.Rect((0, (self.settings.height - self.settings.line)), \
            (self.settings.width, self.settings.line))

        # Dashed line in the center
        center = self.settings.width // 2
        line = self.settings.line
        height = (self.settings.height) - (line * 2)
        segments = 6
        segment_size = height // segments
        self.dashes = [pygame.Rect(center - (line // 2), i, line, segment_size - (segment_size // 5)) \
             for i in range(line + (segment_size // 10), height, height // segments)]

class Ball:
    """
    Defines the ball. Individual functions have to be called independently inside the game loop.
    """

    def __init__(self, settings):
        self.settings = settings
        self.square_x = self.settings.width // 2 - self.settings.line
        self.square_y = self.settings.height // 2 - self.settings.line
        self.size = int(self.settings.line * 1.5)

        self.speed = 2

        self.out_left = False
        self.out_right = False

        self.dir_x = -1
        self.dir_y = -1

        self.square = pygame.Rect(self.square_x, self.square_y, self.size, self.size)

    def movement(self):
        self.square.x += self.dir_x * self.speed
        self.square.y += self.dir_y * self.speed

        return self.square

    def edge_check(self):
        if self.square.top == self.settings.line:
            self.dir_y = -self.dir_y
        elif self.square.bottom == self.settings.height - self.settings.line:
            self.dir_y = -self.dir_y

        return self.dir_x, self.dir_y

    def outside(self):
        if self.square.right < 0:
            self.out_left = True
        elif self.square.left > self.settings.width:
            self.out_right = True

        return self.out_left, self.out_right

    def reset(self):
        if self.out_left or self.out_right:
            time.sleep(1)
            self.square.centerx = self.square_x
            self.square.centery = self.square_y
            self.dir_x = random.choice([-1, 1])
            self.dir_y = random.choice([-1, 1])
            self.out_left = self.out_right = False

class Paddle:
    """
    Defines the paddles.
    """

    def __init__(self, settings, player):
        self.settings = settings
        self.player = player

        self.height = self.settings.height // 5
        self.width = self.settings.line
        self.paddle_init = (self.settings.height // 2) - (self.height // 2)

        if self.player == 1:
            p1_x = self.settings.line * 2
            self.hitter = pygame.Rect(p1_x, self.paddle_init, self.width, self.height)
        else:
            p2_x = self.settings.width - (self.settings.line * 2) - self.width
            self.hitter = pygame.Rect(p2_x, self.paddle_init, self.width, self.height)

    def limits(self):
        if self.hitter.top <= self.settings.line:
            self.hitter.top = self.settings.line
        elif self.hitter.bottom >= self.settings.height - self.settings.line:
            self.hitter.bottom = self.settings.height - self.settings.line

class Score:
    """
    Defines the scoreboards.
    """

    def __init__(self, settings, ball, position):
        self.settings = settings
        self.ball = ball
        self.position = position

        self.score_p1 = 0
        self.score_p2 = 0

        self.board_top = self.settings.height // 10
        self.board_width = self.settings.width // 10
        self.board_height = self.settings.height // 5

        self.board_left = [int(self.settings.width * 0.12), int(self.settings.width * 0.28)]
        self.board_right = [int(self.settings.width * 0.62), int(self.settings.width * 0.78)]

        self.num_left = []
        self.num_right = []

        if self.position:
            for board_start in self.board_left:
                board = pygame.Rect(board_start, self.board_top, self.board_width, self.board_height)
                num = [
                    [board.topleft, board.topright, board.bottomright, board.bottomleft, board.topleft],
                    [board.midtop, board.midbottom],
                    [board.topleft, board.topright, board.midright, board.midleft, board.bottomleft, board.bottomright],
                    [board.topleft, board.topright, board.midright, board.midleft, board.midright, board.bottomright, board.bottomleft],
                    [board.topleft, board.midleft, board.midright, board.topright, board.bottomright],
                    [board.topright, board.topleft, board.midleft, board.midright, board.bottomright, board.bottomleft],
                    [board.topright, board.topleft, board.bottomleft, board.bottomright, board.midright, board.midleft],
                    [board.topleft, board.topright, board.bottomright],
                    [board.topleft, board.topright, board.bottomright, board.bottomleft, board.topleft, board.midleft, board.midright],
                    [board.bottomleft, board.bottomright, board.topright, board.topleft, board.midleft, board.midright]
                    ]
                self.num_left.append(num)
        else:
            boards = self.board_right
            for board_start in boards:
                board = pygame.Rect(board_start, self.board_top, self.board_width, self.board_height)
                num = [
                    [board.topleft, board.topright, board.bottomright, board.bottomleft, board.topleft],
                    [board.midtop, board.midbottom],
                    [board.topleft, board.topright, board.midright, board.midleft, board.bottomleft, board.bottomright],
                    [board.topleft, board.topright, board.midright, board.midleft, board.midright, board.bottomright, board.bottomleft],
                    [board.topleft, board.midleft, board.midright, board.topright, board.bottomright],
                    [board.topright, board.topleft, board.midleft, board.midright, board.bottomright, board.bottomleft],
                    [board.topright, board.topleft, board.bottomleft, board.bottomright, board.midright, board.midleft],
                    [board.topleft, board.topright, board.bottomright],
                    [board.topleft, board.topright, board.bottomright, board.bottomleft, board.topleft, board.midleft, board.midright],
                    [board.bottomleft, board.bottomright, board.topright, board.topleft, board.midleft, board.midright]
                    ]
                self.num_right.append(num)

    def score(self):
        if self.ball.out_left:
            self.score_p2 += 1
        elif self.ball.out_right:
            self.score_p1 += 1

        return self.score_p1, self.score_p2
