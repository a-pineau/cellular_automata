"""Sets the constant variables.

In descending order:
- Window size and font property
- Colours used
- Images (please note that all images used are free to use, links provided below)
"""

import os
import pygame
from pygame.locals import *

pygame.init()
useless_screen = pygame.display.set_mode()
FONT = pygame.font.SysFont("Calibri", 40)

# Directories
FILE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(FILE_DIR, "../imgs")

# Colours
BACKGROUND = pygame.Color(30, 30, 30)
WHITE = pygame.Color(255, 255, 255)
WHITE_2 = pygame.Color(220, 220, 220)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
ALIVE = pygame.Color(46, 204, 113)
BLUE_1 = pygame.Color(158, 190, 228, 255)
BLUE_2 = pygame.Color(0, 216, 219)
YELLOW = pygame.Color(255, 255, 0)
YELLOW_ALPHA = pygame.Color(255, 255, 0, 128)
RED_ALPHA = pygame.Color(255, 0, 0, 128)

# Images
# Cells: https://icons8.com/icons/set/colored-square
DEAD_CELL = pygame.image.load(
    os.path.join(IMAGES_DIR, "dead_cell.png")
    ).convert_alpha()
DEAD_CELL = pygame.transform.rotozoom(DEAD_CELL, 0, 0.2)
X_INFLATE = -4
Y_INFLATE = -4
DEAD_CELL_rect = DEAD_CELL.get_rect().inflate(X_INFLATE, Y_INFLATE)
ALIVE_CELL = pygame.image.load(
    os.path.join(IMAGES_DIR, "alive_cell.png")
    ).convert_alpha()
ALIVE_CELL = pygame.transform.rotozoom(ALIVE_CELL, 0, 0.2)
CELL_SIZE = DEAD_CELL_rect.width
CELL_IMGS = {0: DEAD_CELL, 1: ALIVE_CELL}
# Mouse pointer circle: https://www.iconshock.com/iphone-icons/3d-graphics-icons/circle-icon/
YELLOW_CIRCLE = pygame.image.load(
    os.path.join(IMAGES_DIR, "yellow_circle.png")
    ).convert_alpha()
YELLOW_CIRCLE = pygame.transform.rotozoom(YELLOW_CIRCLE, 0, 0.8) 
YELLOW_CIRCLE.set_alpha(128)
RED_CIRCLE = pygame.image.load(
    os.path.join(IMAGES_DIR, "red_circle.png")
    ).convert_alpha()
RED_CIRCLE = pygame.transform.rotozoom(RED_CIRCLE, 0, 0.8) 
RED_CIRCLE.set_alpha(128)

# Window size (function of number of cells and rectangle inflation)
Y_OFFSET = 65
N_COL = 80
N_ROW = 60
SIZE_X = CELL_SIZE * N_COL - X_INFLATE
SIZE_Y = CELL_SIZE * N_ROW - Y_INFLATE + Y_OFFSET


def main():
    pass

if __name__ == "__main__":
    main()