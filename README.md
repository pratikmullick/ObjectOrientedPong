# Object Oriented Pong
Object Oriented Pong is a modern take on the classic Pong game, with a few hints towards retro console games of the 80s and 90s.  

## Installation
There are multiple ways to install Object Oriented Pong:

- Cloning the repository:

    If you have Python 3 installed on your computer, you can clone the game directly from Github. Use the following command:
    
    ```
    $ git clone https://github.com/pratikmullick/ObjectOrientedPong.git
    ```
    This method should work on Windows, Linux and Mac OS X.

- Windows binary

    A Windows binary distribution is also available <here>. The binary has been tested only on Windows 10.


**Note**: Please make sure that you have Pygame installed on your system. To install Pygame, use:

```
$ pip3 install pygame
```

## Controls
The game allows the user to use the keyboard or gamepad to configure input devices. The default configuration keys are:

+ Select: RETURN
+ Player 1 Up: W
+ Player 1 Down: S
+ Player 2 Up: UP
+ Player 2 Down: DOWN

## Configuration
Object Oriented Pong can be modified by using a simple .pong.conf file, which should be located at the home directory of the user. A copy of the file can be found inside the assets directory, named just 'pong.conf'. The file allows the user to change the following settings:

+ Width: Screen width
+ Height: Screen height
+ Frames: FPS or frames-per-second
+ Keys mentioned above.
+ Max Score for the game.

**Note**: If the '.pong.conf' is not present at the user's home directory, the game will revert back to its default settings.
