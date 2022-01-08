"""Implements the game loop and handles the user's events."""

import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 200)
import math
import pygame
from cellular_automata import CellularAutomata
from constants import *

# Game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode([SIZE_X, SIZE_Y])
    pygame.display.set_caption("Cellular Automata - Game of Life")
    CA = CellularAutomata()
    running = True
    while running:
        # Events handling
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    CA.apply_transition_rules_2()

        CA.display_grid(screen)
        # CA.apply_transition_rules()
        # CA.update_grid()
        pygame.display.update()
        # pygame.time.delay(100)
    pygame.quit()


if __name__ == "__main__":
    main()