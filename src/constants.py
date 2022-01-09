"""Sets the constant variables.

In descending order:
- Window size and font property
- Colours used
- Images (please note that all images used are free to use, links provided below)
- Initial configurations
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
BACKGROUND = (30, 30, 30)
WHITE = (255, 255, 255)
ALIVE = (46, 204, 113)
BLUE_1 = (158, 190, 228, 255)

# Images
# https://icons8.com/icons/set/colored-square
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

# Window size (function of number of cells and rectangle inflation)
YOFFSET = 40
N_COL = 90
N_ROW = 60
SIZE_X = CELL_SIZE * N_COL - X_INFLATE
SIZE_Y = CELL_SIZE * N_ROW - Y_INFLATE + 2 * YOFFSET

# Initial configurations
# Glider
GLIDER = (
    (5,  5),
    (3,  6),
    (5,  6),
    (4,  7),
    (5,  7),
)

def main():
    pass


if __name__ == "__main__":
    main()