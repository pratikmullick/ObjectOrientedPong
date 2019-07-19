#!/usr/bin/env python

# Coding: UTF-8
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

"""
Object Oriented Pong is a clone of the classic Atari arcade game PONG.
Designed with a modern twist, the game retains a few subtle hints towards
classic arcade and console games of yesteryears.

Object Oriented Pong is built with Python 3 and pygame, and is tested with
Python3.6+ and pygame 1.9.4+
"""

import pygame

from options import Configuration
import objects
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
        self.surface.fill(self.confy.navy)

        # Draw Logo
        for letter in objects.Logo(self.confy).logo:
            pygame.draw.lines(self.surface, self.confy.silver, False, letter, self.confy.line)

        # Draw Selection Text
        for msg in self.select.text:
            self.select.font.render_to(self.surface, (self.select.starting, text_init), msg, fgcolor=self.confy.white)
            text_init += self.select.gap

        # Draw Cursor
        pygame.draw.rect(self.surface, self.confy.red, self.cursor)

    def check_cursor_state(self):
        # Checks if cursor is at p1 or p2 position.
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
        # Opening Screen loop
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

    def __init__(self, player, confile=".pong.conf"):
        self.confy = Configuration(confile)
        self.ball = objects.Ball(self.confy)
        self.player = player
        self.borders = objects.Borders(self.confy)
        self.paddle_1 = objects.Paddle(self.confy, 1)
        self.paddle_2 = objects.Paddle(self.confy, 2)
        self.game_functions = functions.Game(self.confy, self.paddle_1, self.paddle_2, self.ball, self.player)
        self.score_1 = objects.Score(self.confy, self.ball, True)
        self.score_2 = objects.Score(self.confy, self.ball, False)

        # Init game screen
        pygame.init()
        pygame.display.set_caption("Object Oriented Pong")
        self.surface = pygame.display.set_mode((self.confy.width, self.confy.height))

    def draw_objects(self):
        self.surface.fill(self.confy.navy)

        # Draw Top and Bottom Borders
        pygame.draw.rect(self.surface, self.confy.silver, self.borders.top_border)
        pygame.draw.rect(self.surface, self.confy.silver, self.borders.bottom_border)

        for dash in self.borders.dashes:
            pygame.draw.rect(self.surface, self.confy.silver, dash)

        # Draw Ball
        pygame.draw.rect(self.surface, self.confy.red, self.ball.square)

        # Draw Paddles
        pygame.draw.rect(self.surface, self.confy.white, self.paddle_1.hitter)
        pygame.draw.rect(self.surface, self.confy.white, self.paddle_2.hitter)

    def ball_functions(self):
        # All interactions with the ball
        self.ball.movement()
        self.ball.edge_check()
        self.ball.outside()
        p1 = self.score_1.score()[0]
        p2 = self.score_2.score()[1]
        self.ball.reset()

        return p1, p2

    def scorecard_display(self):
        # Displaying Scorecard
        val_1, val_2 = self.ball_functions()
        for i in range(2):
            num = self.score_1.num_left
            if i == 1:
                pygame.draw.lines(self.surface, self.confy.white, False, num[i][val_1 % 10], self.confy.line // 2)
            elif i == 0:
                pygame.draw.lines(self.surface, self.confy.white, False, num[i][val_1 // 10], self.confy.line // 2)

        for i in range(2):
            num = self.score_2.num_right
            if i == 1:
                pygame.draw.lines(self.surface, self.confy.white, False, num[i][val_2 % 10], self.confy.line // 2)
            elif i == 0:
                pygame.draw.lines(self.surface, self.confy.white, False, num[i][val_2 // 10], self.confy.line // 2)

    # Game Loop
    def gameloop(self, active=True):
        while active:
            self.game_functions.check_event()
            self.scorecard_display()
            p1, p2 = self.ball_functions()
            if p1 + 1 > self.confy.max_score or p2 + 1 > self.confy.max_score:
                active = False
            self.game_functions.artificial_intelligence()
            self.game_functions.paddle_movement()
            self.game_functions.collision()
            self.draw_objects()
            self.scorecard_display()
            pygame.display.update()
            pygame.time.Clock().tick(self.confy.fps * 2)

def main():
    selection = OpeningScreen().check_cursor_state()
    GameScreen(selection).gameloop()

if __name__ == "__main__":
    main()
