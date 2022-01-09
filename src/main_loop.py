"""Implements the CA loop and handles the user's events."""

import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 100)
import math
import pygame
from cellular_automata import CellularAutomata
from constants import *


def main():
    """Implements Game of Life loop."""
    pygame.init()
    screen = pygame.display.set_mode([SIZE_X, SIZE_Y])
    pygame.display.set_caption("Cellular Automata - Game of Life")
    generation = 0
    waiting_time = 100
    running = True
    pause = True
    CA = CellularAutomata()

    while running:
        # Events handling
        for event in pygame.event.get():
            p_keys = pygame.key.get_pressed()
            p_mouse = pygame.mouse.get_pressed()
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    pause = False if pause else True
                elif event.key == K_p:
                    CA.reset_grid()
                    generation = 0
                    pause = True
            elif event.type == MOUSEBUTTONDOWN and not p_keys[K_LSHIFT]:
                CA.change_cell_state(click=event.button)
            elif p_keys[K_LSHIFT]:
                CA.change_cell_state(pressed=p_mouse)

        if not pause:
            CA.apply_rules()
            generation += 1
            pygame.time.delay(waiting_time)
        CA.display_grid(screen)
        CA.display_stats_cells(screen)
        display_commands(screen)
        screen.blit(FONT.render(f"Generation: {generation}", True, WHITE), (5, 5))
        pygame.display.update()
    pygame.quit()

def display_commands(screen):
    """Display commands at the bottom of the screen."""
    FONT = pygame.font.SysFont("Calibri", 33)
    commands = ("Space: pause/unpause. p: reset. " +
                "L/R click: kill/give birth. " + 
                "Shift+L/R click: multiple selection.")
    commands = FONT.render(commands, True, BLUE_1)
    commands_rect = commands.get_rect()
    commands_rect.left = 5
    commands_rect.top = N_ROW * CELL_SIZE + YOFFSET + 7
    screen.blit(commands, commands_rect)


if __name__ == "__main__":
    main()