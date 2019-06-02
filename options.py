class Options():
    """Stores All Settings"""

    def __init__(self):
        # Screen Settings
        self.x_res = 640
        self.y_res = 480
        self.scr_bg = (0,0,0)
        self.white = (255,255,255)
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
        self.p_length = int(self.y_res / 12)

        # AI settings
        self.wait = 1
        self.difficulty = self.b_speed / 2
