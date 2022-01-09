"""Implements the CA loop and handles the user's events."""

import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 100)
import math
import pygame
from cellular_automata import CellularAutomata
from constants import *

# CA loop
def main():
    pygame.init()
    screen = pygame.display.set_mode([SIZE_X, SIZE_Y])
    pygame.display.set_caption("Cellular Automata - Game of Life")
    CA = CellularAutomata()
    running = True
    pause = True
    waiting = 10000
    while running:
        # Events handling
        CA.display_grid(screen)
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE
                or event.type == QUIT):
                    running = False
            if event.type == KEYDOWN or event.type == KEYUP:
                if event.key == K_SPACE:
                    pause = False
        if not pause:
            CA.apply_rules()
        pygame.display.update()
        pygame.time.delay(100)
    pygame.quit()


if __name__ == "__main__":
    main()