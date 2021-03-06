"""
Defines static and dynamic settings for the other classes to use.
"""

import os
import configparser
import json

class Configuration:
    """
    Checks if a config file is present or not. If present, uses configparser module to load the file.
    """

    def __init__(self, conf_file=".pong.conf"):
        self.conparser = configparser.ConfigParser()
        self.confile = os.path.join(os.path.expanduser("~"), conf_file)
        keymap_file = open('assets/keymaps.json', 'r')
        self.keymaps = json.loads(keymap_file.read())

        if os.path.isfile(self.confile):
            # print("Configs: Reading from", self.confile)    # Debug Line
            self.conparser.read(self.confile)
            self.width = int(self.conparser['SCREEN']['Width'])
            self.height = int(self.conparser['SCREEN']['Height'])
            self.fps = int(self.conparser['SCREEN']['Frames'])

            # Keys
            self.select_key = int(self.keymaps[self.conparser['KEY']['Select']])
            self.p1_up = int(self.keymaps[self.conparser['KEY']['P1_UP']])
            self.p1_down = int(self.keymaps[self.conparser['KEY']['P1_DOWN']])
            self.p2_up = int(self.keymaps[self.conparser['KEY']['P2_UP']])
            self.p2_down = int(self.keymaps[self.conparser['KEY']['P2_DOWN']])
            self.max_score = int(self.conparser['SCORE']['MAX'])

            if self.max_score > 99:
                self.max_score = 99

        else:
            # print("Configs:", self.confile, "not found! Using Defaults")   # Debug Line
            self.width = 640
            self.height = 480
            self.fps = 180
            self.select_key = int(self.keymaps['RETURN'])
            self.p1_up = int(self.keymaps['w'])
            self.p1_down = int(self.keymaps['s'])
            self.p2_up = int(self.keymaps['UP'])
            self.p2_down = int(self.keymaps['DOWN'])
            self.max_score = 10


        # Static Options
        self.line = self.width // 50
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.silver = (192, 192, 192)
        self.navy = (13, 0, 77)
        self.red = (255, 0, 0)
