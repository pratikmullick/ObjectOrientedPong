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
    
    def __init__(self, confile=".pong.conf"):
        self.confy = Configuration(confile)
        self.borders = objects.Borders(self.confy)

        # Init game screen
        pygame.init()
        self.surface = pygame.display.set_mode((self.confy.width, self.confy.height))
        
        self.draw_objects()
        pygame.display.update()
        
    def draw_objects(self):
        self.surface.fill(self.confy.black)
        
        # Draw Top and Bottom Borders
        pygame.draw.rect(self.surface, (255, 0, 0), self.borders.top_border)
        pygame.draw.rect(self.surface, (255, 0, 0), self.borders.bottom_border)
        # pygame.draw.rect(self.surface, (0, 0, 255), self.borders.dash)
        
        for i in self.borders.dashes:
            pygame.draw.rect(self.surface, self.confy.white, i)

if __name__ == "__main__":
    OpeningScreen().check_cursor_state()
    GameScreen()
    time.sleep(10)
