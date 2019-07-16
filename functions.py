import os, sys
import pygame

class Opening:
    """
    Functions for moving the cursor on the opening screen.
    """
    
    def __init__(self):
        pygame.init()
        self.state = 1
        self.start = False

    def check_event(self):
        for event in pygame.event.get():
            # For exiting out of the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # For moving the cursor.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print("Down")
                    self.state = 2
                if event.key == pygame.K_UP:
                    print("UP")
                    self.state = 1
                if event.key == pygame.K_RETURN:
                    self.start = True
"""
class Game:
    """
    Functions for moving the paddle in the game.
    """
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
