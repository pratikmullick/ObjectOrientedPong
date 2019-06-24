import os
import sys
import configparser

class Configuration:
    """
    Checks if a config file is present or not. If present, uses configparser module to load the file.
    """

    def __init__(self, conf_file):
        self.conparser = configparser.ConfigParser()
        self.confile = os.path.join(os.path.expanduser("~"), conf_file)

        if os.path.isfile(self.confile):
            print("Configs: Reading from", self.confile)    # Debug Line
            self.conparser.read(self.confile)
            self.width = int(self.conparser['SCREEN']['Width'])
            self.height = int(self.conparser['SCREEN']['Height'])
            self.fps = int(self.conparser['SCREEN']['Frames'])
        else:
            print("Configs:", self.confile, "not found! Using Defaults")   # Debug Line

# Debug

if __name__ == "__main__":
    test = Configuration(".pong.conf")
