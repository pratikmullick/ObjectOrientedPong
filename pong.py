import pygame
import random,time,sys

class Settings():
    """Stores All Settings"""

    def __init__(self):
        # Screen Settings
        self.x_res = 640
        self.y_res = 480
        self.scr_bg = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.fps = 180

        # Line Settings
        self.line = 10
        self.ctr_segment = 12

        # Key Settings
        self.exit_key = pygame.K_ESCAPE

        # Ball Settings
        self.b_size = int(self.line*2)
        self.b_speed = 2

        # Paddle Settings
        self.p_width = self.line * 2
        self.p_length = 50

class GameFunctions():
    """A Class to store game functions"""

    def __init__(self,sett,p1,p2,ball):
        self.sett = Settings()
        self.p1 = p1.paddle
        self.p2 = p2.paddle
        self.p1_score = 0
        self.p2_score = 0
        self.ball = ball

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
                self.p2.y += self.sett.b_speed
            elif self.p2.centery > self.sett.y_res / 2:
                self.p2.y -= self.sett.b_speed
        # Track ball when ball moves towards paddle
        elif self.ball.balldir_x == 1:
            if self.p2.centery < self.ball.ball.centery:
                self.p2.y += self.sett.b_speed
            else:
                self.p2.y -= self.sett.b_speed

    def score(self):
        if self.ball.ball.right < 0:
            self.p2_score += 1
            time.sleep(1)
            self.ball.ball.centerx = self.ball.b_x
            self.ball.ball.centery = self.ball.b_y
        elif self.ball.ball.left > self.sett.x_res:
            self.p1_score += 1
            time.sleep(1)
            self.ball.ball.centerx = self.ball.b_x
            self.ball.ball.centery = self.ball.b_y

class Screen():
    """Screen settings and rendering"""

    def __init__(self,s,ball,p1,p2):
        self.s = s
        self.surface = pygame.display.set_mode((self.s.x_res,self.s.y_res))
        self.ball = ball
        self.p1 = p1.paddle
        self.p2 = p2.paddle

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
        pygame.draw.rect(self.surface,self.s.red,self.ball.ball)
        pygame.draw.rect(self.surface,self.s.white,self.p1)
        pygame.draw.rect(self.surface,self.s.white,self.p2)
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

def main():
    """Main Program"""

    sett = Settings()
    ball = Ball(sett)
    paddle_1 = Paddle(sett,True)
    paddle_2 = Paddle(sett,False)
    gf = GameFunctions(sett,paddle_1,paddle_2,ball)
    screen = Screen(sett,ball,paddle_1,paddle_2)

    active = True

    while active:
        screen.render_scr()
        gf.check_input()
        ball.move_ball()
        gf.artificial_intelligence()
        ball.check_edges()
        paddle_1.limits()
        gf.paddle_collision()
        gf.score()
        screen.update_scr()

main()
