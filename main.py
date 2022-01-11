"""Implements the CA loop and handles the user's events."""

import sys
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 100)
sys.path.insert(0, "C:/Users/Adrian/Desktop/Python/CellularAutomata_GameOfLife/src")

import math
import pygame

from pygame import gfxdraw
from cellular_automata import CellularAutomata
from constants import *

def main():
    """Implements Game of Life loop."""
    pygame.init()
    screen = pygame.display.set_mode([SIZE_X, SIZE_Y])
    clock = pygame.time.Clock()
    fps = 75
    pygame.display.set_caption("Cellular Automata - Game of Life")
    generation = 0
    waiting_time = 100
    running = True
    pause = True
    show_commands = False
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
                    fps = 15 if not pause else 75
                elif event.key == K_p:
                    CA.reset_grid()
                    generation = 0
                    pause = True
                    fps = 75
                elif event.key == K_F1:
                    show_commands = True if not show_commands else False
            elif event.type == MOUSEBUTTONDOWN and not p_keys[K_LSHIFT]:
                CA.change_cell_state(click=event.button)
            elif p_keys[K_LSHIFT]:
                draw_circle_pointer = True
                CA.change_cell_state(pressed=p_mouse)
            else:
                draw_circle_pointer = False

        if not pause:
            CA.apply_rules()
            generation += 1
        CA.display_grid(screen)
        if show_commands:
            display_commands(screen)
        if draw_circle_pointer:
            draw_circle_selection(screen, p_mouse)
        display_menu(screen)
        screen.blit(FONT.render(f"Generation: {generation}", True, WHITE), (5, 5))
        display_FPS(screen, clock)
        alive, percentage = CA.get_stats_cells()
        display_cells_stats(screen, alive, percentage)
        display_progress_bar(screen, percentage)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()

def draw_circle_selection(screen, pressed):
    """Draws a circle centered around the mouse pointer.

    The circle is drawn when holding shift and pressing left or right 
    mouse click. If the left mouse click is held, the circle is yellow (giving birth to cells).
    Its red otherwise (killing cells).

    Parameter
    ---------
    screen: pygame.Surface
    """
    # left or right click
    if pressed[0] or pressed[2]:
        x, y = pygame.mouse.get_pos()
        circle = YELLOW_CIRCLE if pressed[0] else RED_CIRCLE
        circle_rect = circle.get_rect(center=(x, y))
        if pygame.mouse.get_focused():
            screen.blit(circle, circle_rect)

def display_cells_stats(screen, alive, percentage):
    """Display cells statistics (top-right)."""
    stats = f"{alive} Cells alive ({percentage}%)"
    stats = FONT.render(stats, True, ALIVE)
    stats_rect = stats.get_rect()
    stats_rect.right = N_COL * CELL_SIZE
    stats_rect.top = 5
    screen.blit(stats, stats_rect)

def display_progress_bar(screen, percentage):
    """Display a progress bar for alive cells (top-right)."""
    start = SIZE_X * 0.675
    end_background = SIZE_X - start - 8
    width = 15
    bar_background_rect = pygame.Rect(start, 48, end_background, width)
    end_foreground = (percentage / 100) * end_background
    bar_foreground_rect = pygame.Rect(start, 48, end_foreground, width)
    pygame.draw.rect(screen, WHITE_2, bar_background_rect)
    pygame.draw.rect(screen, ALIVE, bar_foreground_rect)

def display_FPS(screen, clock):
    """Display FPS (top-center)."""
    n_fps = int(clock.get_fps())
    fps_text = FONT.render(f"FPS: {n_fps}", True, YELLOW)
    fps_text_rect = fps_text.get_rect()
    fps_text_rect.centerx = SIZE_X // 2
    fps_text_rect.top = 5
    screen.blit(fps_text, fps_text_rect)

def display_menu(screen):
    """Displays how to show game commands (top-left).
    
    Parameter
    ---------
    screen: pygame.Surface
        Game window
    """
    FONT = pygame.font.SysFont("Calibri", 29)
    text_menu = FONT.render("Toggle F1 to show game commands", True, BLUE_2)
    text_menu_rect = text_menu.get_rect()
    text_menu_rect.left = 5
    text_menu_rect.top = 39
    screen.blit(text_menu, text_menu_rect)

def display_commands(screen):
    """Displays commands at the bottom of the screen.

    Parameter
    ---------
    screen: pygame.Surface
        Game window
    """

    FONT = pygame.font.SysFont("Calibri", 33)
    start_y = 85
    left_anchor = 5
    sep = 35
    # spacebar
    cmd_space = FONT.render("Space: pause/unpause the game", True, WHITE)
    cmd_space_rect = cmd_space.get_rect()
    cmd_space_rect.left = left_anchor
    cmd_space_rect.top = start_y
    # key p
    cmd_p = FONT.render("p: reset game", True, WHITE)
    cmd_p_rect = cmd_space.get_rect()
    cmd_p_rect.left = left_anchor
    start_y += sep
    cmd_p_rect.top = start_y
    # left/right click
    cmd_lr_click = FONT.render("Left/right click: kill/give birth to a cell", True, WHITE)
    cmd_lr_click_rect = cmd_space.get_rect()
    cmd_lr_click_rect.left = left_anchor
    start_y += sep
    cmd_lr_click_rect.top = start_y
    # shift + left/right click
    cmd_shift_lr_click = FONT.render("Shift + left/right click: multiple kills/births", True, WHITE)
    cmd_shift_lr_click_rect = cmd_space.get_rect()
    cmd_shift_lr_click_rect.left = left_anchor
    start_y += sep
    cmd_shift_lr_click_rect.top = start_y
    # blit all
    screen.blit(cmd_space, cmd_space_rect)
    screen.blit(cmd_p, cmd_p_rect)
    screen.blit(cmd_lr_click, cmd_lr_click_rect)
    screen.blit(cmd_shift_lr_click, cmd_shift_lr_click_rect)


if __name__ == "__main__":
    main()