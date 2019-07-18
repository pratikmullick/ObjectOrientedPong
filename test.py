from options import Configuration
import objects
import pygame
import time
import functions

class OpeningScreen:
    """
    Draws Opening Screen on to the desktop window.
    """
    
    def __init__(self, confile=".pong.conf"):
        self.confy = Configuration(confile)
        self.opening = functions.Opening(self.confy)
        self.select = objects.Selection(self.confy)
        self.cursor = self.select.cursor

        # Init game screen
        pygame.init()
        self.surface = pygame.display.set_mode((self.confy.width, self.confy.height))

        # Run Loop
        self.loop()

    def draw_objects(self):
        text_init = self.select.position
        self.surface.fill(self.confy.black)
        
        # Draw Logo
        for letter in objects.Logo(self.confy).logo:
            pygame.draw.lines(self.surface, self.confy.silver, False, letter, self.confy.line)

        # Draw Selection Text
        for msg in self.select.text:
            self.select.font.render_to(self.surface, (self.select.starting,text_init), msg, fgcolor=self.confy.white)
            text_init += self.select.gap

        pygame.draw.rect(self.surface, self.confy.white, self.cursor)

    def check_cursor_state(self):
        self.opening.check_event()
        if self.opening.state == 2:
            self.cursor.top = self.select.position + self.select.gap
        elif self.opening.state == 1:
            self.cursor.top = self.select.position
        if self.opening.state == 1 and self.opening.start == True:
            return self.opening.state
        elif self.opening.state == 2 and self.opening.start == True:
            return self.opening.state

    def loop(self):
        while True:
            fps_clock = pygame.time.Clock()
            self.check_cursor_state()
            if self.opening.start == True:
                break
            self.draw_objects()
            pygame.display.update()
            fps_clock.tick(self.confy.fps)

class GameScreen:
    """
    Draws the GameScreen on the Window.
    """
    
    def __init__(self, ball, player, confile=".pong.conf"):
        self.confy = Configuration(confile)
        self.ball = ball
        self.player = player
        self.borders = objects.Borders(self.confy)
        self.paddle_1 = objects.Paddle(self.confy, 1)
        self.paddle_2 = objects.Paddle(self.confy, 2)
        self.game_functions = functions.Game(self.confy, self.paddle_1, self.paddle_2, self.ball, self.player)
        
        # Init game screen
        pygame.init()
        self.surface = pygame.display.set_mode((self.confy.width, self.confy.height))

    def draw_objects(self):
        self.surface.fill(self.confy.black)
        
        # Draw Top and Bottom Borders
        pygame.draw.rect(self.surface, self.confy.silver, self.borders.top_border)
        pygame.draw.rect(self.surface, self.confy.silver, self.borders.bottom_border)
        
        for dash in self.borders.dashes:
            pygame.draw.rect(self.surface, self.confy.silver, dash)

        # Draw Ball
        pygame.draw.rect(self.surface, self.confy.white, self.ball.square)
        
        # Draw Paddles
        pygame.draw.rect(self.surface, self.confy.white, self.paddle_1.hitter)
        pygame.draw.rect(self.surface, self.confy.white, self.paddle_2.hitter)
        
    def ball_functions(self):
        self.ball.movement()
        self.ball.edge_check()
        self.ball.outside()
        self.ball.reset()
        
    # Game Loop for One-Player
    def gameloop(self):
        while True:
            self.game_functions.check_event()
            self.ball_functions()
            self.game_functions.artificial_intelligence()
            self.game_functions.paddle_movement()
            self.game_functions.collision()
            self.draw_objects()
            pygame.display.update()
            pygame.time.Clock().tick(360)


if __name__ == "__main__":
    ball = objects.Ball(Configuration())
    selection = OpeningScreen().check_cursor_state()
    GameScreen(ball, selection).gameloop()
    
