import os
import sys

"""1. Checks if .pong directory is present or not, then copies default config"""
"""2. If default config is present, reads from file to create settings"""

class Configs:
    """Checks for .pong directory"""

    def __init__(self, pong_dir):
        self.confile = ".pong.conf"
        self.home_dir = os.path.expanduser("~")

        if os.path.isfile(os.path.join(self.home_dir, self.confile)):
            print("Configs: Reading from pong.")
        else:
            print("NO DIR")

if __name__ == "__main__":
    test = Configs(".pong")
