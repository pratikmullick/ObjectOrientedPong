import os, sys
import pygame
import objects

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

            # For exiting out of the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # For moving the cursor.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.down = event.key
                    self.state = 2
                if event.key == pygame.K_UP:
                    self.up = event.key
                    self.state = 1

            # For selecting
                if event.key == self.settings.select_key:
                    self.start = True

class Game:
    """
    Functions for the control of objects within the game.
    """
    def __init__(self, settings, paddle_1, paddle_2, ball, player):
        pygame.init()
        self.settings = settings
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.ball = ball
        self.player = player
        
        self.speed = 5
        self.p1_up = False
        self.p1_down = False
        self.p2_up = False
        self.p2_down = False
    
    def check_event(self):
        for event in pygame.event.get():
            # For exiting out of the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Checking up and down movements from p1
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings.p1_up:
                    self.p1_up = True
            elif event.type == pygame.KEYUP:
                if event.key == self.settings.p1_up:
                    self.p1_up = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings.p1_down:
                    self.p1_down = True
            elif event.type == pygame.KEYUP:
                if event.key == self.settings.p1_down:
                    self.p1_down = False
                    
            # Checking up and down movements from p2
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings.p2_up:
                    self.p2_up = True
            elif event.type == pygame.KEYUP:
                if event.key == self.settings.p2_up:
                    self.p2_up = False
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings.p2_down:
                    self.p2_down = True
            elif event.type == pygame.KEYUP:
                if event.key == self.settings.p2_down:
                    self.p2_down = False

    def paddle_movement(self):
        if self.player == 1:
            if self.p1_up:
                self.paddle_1.hitter.centery -= self.speed
            elif self.p1_down:
                self.paddle_1.hitter.centery += self.speed
        if self.player == 2:
            if self.p1_up:
                self.paddle_1.hitter.centery -= self.speed
            elif self.p1_down:
                self.paddle_1.hitter.centery += self.speed
            if self.p2_up:
                self.paddle_2.hitter.centery -= self.speed
            elif self.p2_down:
                self.paddle_2.hitter.centery += self.speed
        self.paddle_1.limits()
        self.paddle_2.limits()

    def collision(self):
        if pygame.Rect.colliderect(self.ball.square, self.paddle_1.hitter):
            self.ball.dir_x = -self.ball.dir_x
        elif pygame.Rect.colliderect(self.ball.square, self.paddle_2.hitter):
            self.ball.dir_x = -self.ball.dir_x
            
    def artificial_intelligence(self):
        """
        More work needed here!
        """
        if self.player == 1:
            self.paddle_2.hitter.centery = self.ball.square.centery

    