# Coding: ASCII
# Object Oriented Pong - A Classic Atari Pong Clone
# Copyright (C) 2018  Pratik Mullick

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Pratik Mullick
# pratik.mullick@gmail.com

"""Object Oriented Pong is a clone of the classic Atari arcade game PONG.
Designed as close as possible to the classic Arcade game, the game currently
supports one-player mode with an AI opponent.

Object Oriented Pong is built with Python 3 and pygame, and is tested with
Python3.6. and pygame 1.9.4."""

import pygame
import settings
import random,time,sys

class GameFunctions():
    """A Class to store game functions"""

    def __init__(self,sett,p1,p2,ball):
        self.sett = Settings()
        self.p1 = p1.paddle
        self.p2 = p2.paddle
        self.ball = ball
        self.b_rect = self.ball.ball

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == self.sett.exit_key:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                m_x,m_y = event.pos
                self.p1.y = m_y

    def paddle_collision(self):
        """Detects Collision between ball and paddle"""
        if pygame.Rect.colliderect(self.p1,self.ball.ball):
            self.ball.balldir_x = -self.ball.balldir_x
        elif pygame.Rect.colliderect(self.p2,self.ball.ball):
            self.ball.balldir_x = -self.ball.balldir_x

    def artificial_intelligence(self):
        """This AI Cheats!"""
        # Center paddle when ball moves away
        if self.ball.balldir_x == -1:
            if self.p2.centery < self.sett.y_res / 2:
                self.p2.y += self.sett.difficulty
            elif self.p2.centery > self.sett.y_res / 2:
                self.p2.y -= self.sett.difficulty
        # Track ball when ball moves towards paddle
        elif self.ball.balldir_x == 1:
            if self.p2.centery < self.ball.ball.centery:
                self.p2.y += self.sett.difficulty
            else:
                self.p2.y -= self.sett.difficulty

    def reset(self):
        if self.ball.out_left == True or self.ball.out_right == True:
            time.sleep(self.sett.wait)
            self.b_rect.centerx = self.ball.b_x
            self.b_rect.centery = self.ball.b_y
            self.ball.balldir_x = random.choice([-1,1])
            self.ball.balldir_y = random.choice([-1,1])
            self.ball.out_left = self.ball.out_right = False

class GameScreen():
    """Screen settings and rendering"""

    def __init__(self,s,ball,p1,p2,score1,score2):
        self.s = s
        self.surface = pygame.display.set_mode((self.s.x_res,self.s.y_res))
        self.ball = ball.ball
        self.p1 = p1.paddle
        self.p2 = p2.paddle
        self.score_1 = score1
        self.score_2 = score2

    def render_scr(self):
        pygame.init()
        pygame.display.set_caption("PONG")
        self.surface.fill(self.s.scr_bg)

        # Render Top Line and Bottom Line
        pygame.draw.line(self.surface, self.s.white, (0,0), \
                (self.s.x_res,0), self.s.line*2)

        pygame.draw.line(self.surface,self.s.white,(0,self.s.y_res), \
                (self.s.x_res,self.s.y_res), self.s.line*2)

        # Render Dashed Line with Segments
        x_scr_ctr = int(self.s.x_res/2)
        y_gap = int(self.s.y_res/self.s.ctr_segment)

        for i in range(0, self.s.y_res, y_gap):
            if i % y_gap == 0:
                pygame.draw.line(self.surface, self.s.white, \
                        (x_scr_ctr,i+int(y_gap/4)), \
                        (x_scr_ctr,i+int(y_gap*0.75)), int(self.s.line/2))

    def update_scr(self):
        fps_clock = pygame.time.Clock()
        pygame.draw.rect(self.surface,self.s.white,self.ball)
        pygame.draw.rect(self.surface,self.s.white,self.p1)
        pygame.draw.rect(self.surface,self.s.white,self.p2)
        pygame.draw.lines(self.surface,self.s.white,False, \
                            self.score_1.num[self.score_2.val_1], \
                        self.s.line)
        pygame.draw.lines(self.surface,self.s.white,False, \
                            self.score_2.num[self.score_2.val_2], \
                        self.s.line)
        pygame.display.update()
        fps_clock.tick(self.s.fps)

class Ball():
    """Object representation of Ball"""

    def __init__(self,s):
        self.s = s
        self.b_x = int(self.s.x_res/2) - self.s.line
        self.b_y = int(self.s.y_res/2) - self.s.line
        self.balldir_x = -1
        self.balldir_y = -1
        self.ball = pygame.Rect(self.b_x,self.b_y,self.s.b_size,self.s.b_size)
        self.out_left = False
        self.out_right = False

    def move_ball(self):
        self.ball.x += (self.balldir_x * self.s.b_speed)
        self.ball.y += (self.balldir_y * self.s.b_speed)
        return self.ball

    def check_edges(self):
        if self.ball.top == self.s.line:
            self.balldir_y = -self.balldir_y
        elif self.ball.bottom == self.s.y_res - (self.s.line):
            self.balldir_y = -self.balldir_y

        return self.balldir_x,self.balldir_y

    def check_out(self):
        if self.ball.right < 0:
            self.out_left = True
        elif self.ball.left > self.s.x_res:
            self.out_right = True

class Paddle():
    """Object definition and functions of Paddles"""

    def __init__(self,s,p1):
        self.s = s
        self.p1 = p1
        self.hgt = self.s.p_length
        self.wdt = self.s.p_width
        p1_x = self.s.line*2
        p1_y = int(self.s.y_res/2)
        p2_x = self.s.x_res - (self.s.line*2) - self.wdt
        p2_y = int(self.s.y_res/2)

        if self.p1:
            self.paddle = pygame.Rect(p1_x,p1_y,self.wdt,self.hgt)
        else:
            self.paddle = pygame.Rect(p2_x,p2_y,self.wdt,self.hgt)

    def limits(self):
        if self.paddle.top < self.s.line * 2:
            self.paddle.top = self.s.line * 2
        elif self.paddle.bottom > self.s.y_res - (self.s.line * 2):
            self.paddle.bottom = self.s.y_res - (self.s.line * 2)

class Score():
    """Maintain and Display Score"""
    def __init__(self,sett,ball,position):
        self.sett = sett
        self.ball = ball
        self.position = position
        self.val_1 = 0
        self.val_2 = 0

        self.s_x = int(self.sett.x_res * 0.25) - self.sett.line * 2
        self.s_y = int(self.sett.y_res * 0.10)
        self.s_w = int(self.sett.x_res * 0.10) - self.sett.line * 2
        self.s_h = int(self.sett.y_res * 0.15)

        if  not self.position:
            self.s_x *= 3

        self.board = pygame.Rect(self.s_x,self.s_y,self.s_w,self.s_h)

        self.num = [
                        [
                        self.board.topleft,self.board.topright,
                        self.board.bottomright,self.board.bottomleft,
                        self.board.topleft
                        ],
                        [
                        self.board.midtop,self.board.midbottom
                        ],
                        [
                        self.board.topleft,self.board.topright, \
                        self.board.midright,self.board.midleft, \
                        self.board.bottomleft,self.board.bottomright
                        ],
                        [
                        self.board.topleft,self.board.topright,
                        self.board.midright,self.board.midleft,
                        self.board.midright,self.board.bottomright,
                        self.board.bottomleft
                        ],
                        [
                        self.board.topleft,self.board.midleft, \
                        self.board.midright,self.board.topright, \
                        self.board.bottomright
                        ],
                        [
                        self.board.topright,self.board.topleft, \
                        self.board.midleft,self.board.midright, \
                        self.board.bottomright,self.board.bottomleft
                        ],
                        [
                        self.board.topright,self.board.topleft, \
                        self.board.bottomleft,self.board.bottomright, \
                        self.board.midright,self.board.midleft
                        ],
                        [
                        self.board.topleft,self.board.topright, \
                        self.board.bottomright
                        ],
                        [
                        self.board.topleft,self.board.topright, \
                        self.board.bottomright,self.board.bottomleft, \
                        self.board.topleft,self.board.midleft, \
                        self.board.midright
                        ],
                        [
                        self.board.bottomleft,self.board.bottomright, \
                        self.board.topright,self.board.topleft, \
                        self.board.midleft,self.board.midright
                        ]
                    ]

    def check_value(self):
        if self.ball.out_left == True:
            self.val_2 += 1
            return self.val_1
        elif self.ball.out_right == True:
            self.val_1 += 1
            return self.val_2

def main(active=True):
    """Main Program"""

    sett = Settings()
    ball = Ball(sett)
    paddle_1 = Paddle(sett,True)
    paddle_2 = Paddle(sett,False)
    scoreclass1 = Score(sett,ball,True)
    scoreclass2 = Score(sett,ball,False)
    gf = GameFunctions(sett,paddle_1,paddle_2,ball)
    g_scr = GameScreen(sett,ball,paddle_1,paddle_2,scoreclass1,scoreclass2)

    while active:
        g_scr.render_scr()
        gf.check_input()
        ball.move_ball()
        gf.artificial_intelligence()
        ball.check_edges()
        ball.check_out()
        paddle_1.limits()
        gf.paddle_collision()
        scoreclass1.check_value()
        scoreclass2.check_value()
        gf.reset()
        g_scr.update_scr()
        if scoreclass1.val_1 >= 9 or scoreclass2.val_2 >= 9:
            active = False

if __name__ == "__main__":
    main()
