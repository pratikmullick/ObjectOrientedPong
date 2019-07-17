import os, sys
import pygame

class Opening:
    """
    Functions for moving the cursor on the opening screen.
    """
    
    def __init__(self, settings):
        pygame.init()
        self.settings = settings

        self.state = 1
        self.start = False
        self.down = 0
        self.up = 0

    def check_event(self):
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            # For exiting out of the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # For moving the cursor.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.down = event.key
                    print(self.down)
                    self.state = 2
                if event.key == pygame.K_UP:
                    self.up = event.key
                    print(self.up)
                    self.state = 1
                if event.key == self.settings.select_key:
                    self.start = True

"""
class Game:
    def __init__(self):
        pygame.init()
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left")
                if event.key == pygame.K_RIGHT:
                    print("Right")
"""

if __name__ == "__main__":
    while True:
        pygame.init()
        pygame.display.set_mode((640, 480))
        Opening().check_event()
        if Opening().check_event() != 0:
            print(Opening().up, Opening().down)
        pygame.display.update()
        
        
