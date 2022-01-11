"""Implements the CA loop and handles the user's events."""

import sys
import os
import win32api
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 100)
sys.path.insert(0, "C:/Users/Adrian/Desktop/Python/CellularAutomata_GameOfLife/src")

import math
import pygame
from pygame import gfxdraw

from cellular_automata import CellularAutomata
from constants import *
SNAP_FOLDER = os.path.join(os.path.dirname(__file__), "results")
n_snap = 0


def main():
    """Implements the main loop."""
    monitor = win32api.EnumDisplayDevices()
    try:
        os.mkdir(SNAP_FOLDER)
    except FileExistsError:
        print(f"Folder \"{SNAP_FOLDER}\" already exists. Ignoring.")
    if os.path.isdir(SNAP_FOLDER):
        for file_name in os.listdir(SNAP_FOLDER):
            file = os.path.join(SNAP_FOLDER, file_name)
            os.remove(file)

    pygame.init()
    screen = pygame.display.set_mode([SIZE_X, SIZE_Y])
    clock = pygame.time.Clock()
    native_fps = get_freqrate_monitor(monitor)
    playing_fps = 15
    fps = native_fps
    pygame.display.set_caption("Cellular Automata - Game of Life")
    generation = 0
    waiting_time = 100
    running = True
    pause = True
    show_commands = False
    record = False
    taking_snapshot = False
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
                    fps = playing_fps if not pause else native_fps
                elif event.key == K_p:
                    CA.reset_grid()
                    generation = 0
                    pause = True
                    fps = native_fps
                elif event.key == K_F1:
                    show_commands = True if not show_commands else False
                elif event.key == K_F2:
                    taking_snapshot = True
                elif event.key == K_F3:
                    record = True if not record else False
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
        display_generation(screen, generation)
        display_FPS(screen, clock)
        display_record_state(screen, record)
        alive, percentage = CA.get_stats_cells()
        display_cells_stats(screen, alive, percentage)
        display_progress_bar(screen, percentage)
        if record or taking_snapshot:
            record_game(screen)
        clock.tick(fps)
        taking_snapshot = False

        # Updating screen state
        pygame.display.update()
    # Closing window
    pygame.quit()

def get_freqrate_monitor(device) -> int:
    """Returns the frequency rate (in Hz) of the monitor used.

    Parameter
    ---------
    device: PyDISPLAY_DEVICE (required)
        User's monitor
    """

    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, "DisplayFrequency")

def record_game(screen) -> None:
    """Save a snapshot of the current grid to the SNAP_FOLDER.

    Parameter
    ---------
    screen: pygame.Surface (required)
        Game window
    """

    global n_snap
    n_snap += 1
    extension = "png"
    file_name = f"snapshot_{n_snap}.{extension}"
    pygame.image.save(screen, os.path.join(SNAP_FOLDER, file_name))

def draw_circle_selection(screen, pressed) -> None:
    """Draws a circle centered around the mouse pointer.

    The circle is drawn when holding shift and pressing left or right 
    mouse click. If the left mouse click is held, the circle is yellow (giving birth to cells).
    Its red otherwise (killing cells).

    Parameter
    ---------
    screen: pygame.Surface (required)
        Game window
    pressed: bool (required)
        True if any mouseclick is pressed, False otherwise
    """

    # left or right click
    if pressed[0] or pressed[2]:
        x, y = pygame.mouse.get_pos()
        circle = YELLOW_CIRCLE if pressed[0] else RED_CIRCLE
        circle_rect = circle.get_rect(center=(x, y))
        if pygame.mouse.get_focused():
            screen.blit(circle, circle_rect)

def display_generation(screen, generation) -> None:
    """Display the current number of generations (top-left)

    Parameters
    ----------
    screen: pygame.Surface (required)
        Game window
    generation: int (required)
        Current number of generations
    """

    gen = FONT.render(f"Generation: {generation}", True, WHITE)
    gen_rect = gen.get_rect()
    gen_rect.left = 5
    gen_rect.top = 5
    screen.blit(gen, gen_rect)

def display_record_state(screen, record) -> None:
    """Display the current state of the record mode (top-center).

    Parameters
    ----------
    screen: pygame.Surface (required)
        Game window
    record: bool (required)
        True if record mode is enabled, False otherwise
    """
    
    FONT = pygame.font.SysFont("Calibri", 29)
    if record:
        record_state = FONT.render("Recording", True, GREEN)
    else:
        record_state = FONT.render("Not recording", True, RED)
    record_state_rect = record_state.get_rect()
    record_state_rect.centerx = SIZE_X / 2
    record_state_rect.top = 39
    screen.blit(record_state, record_state_rect)

def display_cells_stats(screen, alive, percentage) -> None:
    """Display cells statistics (top-right).

    Parameters
    ----------
    screen: pygame.Surface (required)
        Game window
    alive: int (required)
        Current number of cells alive
    percentage: float (required)
        Current percentage of cells alive
    """

    stats = f"{alive} Cells alive ({percentage}%)"
    stats = FONT.render(stats, True, ALIVE)
    stats_rect = stats.get_rect()
    stats_rect.right = N_COL * CELL_SIZE
    stats_rect.top = 5
    screen.blit(stats, stats_rect)

def display_progress_bar(screen, percentage) -> None:
    """Display a progress bar for alive cells (top-right).

    Parameters
    ----------
    screen: pygame.Surface (required)
        Game window
    percentage: float (required)
        Current percentage of cells alive
    """

    start = SIZE_X * 0.675
    end_background = SIZE_X - start - 8
    width = 15
    bar_background_rect = pygame.Rect(start, 48, end_background, width)
    end_foreground = (percentage / 100) * end_background
    bar_foreground_rect = pygame.Rect(start, 48, end_foreground, width)
    pygame.draw.rect(screen, WHITE_2, bar_background_rect)
    pygame.draw.rect(screen, ALIVE, bar_foreground_rect)

def display_FPS(screen, clock):
    """Display FPS (top-center).

    Parameters
    ----------
    screen: pygame.Surface (required)
        Game window
    clock: Clock (required)
        Pygame internal clock
    """

    n_fps = int(clock.get_fps())
    fps_text = FONT.render(f"FPS: {n_fps}", True, YELLOW)
    fps_text_rect = fps_text.get_rect()
    fps_text_rect.centerx = SIZE_X // 2
    fps_text_rect.top = 5
    screen.blit(fps_text, fps_text_rect)

def display_menu(screen) -> None:
    """Displays how to show game commands (top-left).
    
    Parameter
    ---------
    screen: pygame.Surface (required)
        Game window
    """
    FONT = pygame.font.SysFont("Calibri", 29)
    text_menu = FONT.render("Press F1 to show game commands", True, BLUE_2)
    text_menu_rect = text_menu.get_rect()
    text_menu_rect.left = 5
    text_menu_rect.top = 39
    screen.blit(text_menu, text_menu_rect)

def display_commands(screen) -> None:
    """Displays commands (top-left).

    Since Pygame doesn't allow (to my knowledge) line breaks when
    rendering fonts, the commands are split into lines separately.

    Parameter
    ---------
    screen: pygame.Surface (required)
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
    # F1
    cmd_F1 = FONT.render("F1: show/hide menu", True, WHITE)
    cmd_F1_rect = cmd_space.get_rect()
    cmd_F1_rect.left = left_anchor
    start_y += sep
    cmd_F1_rect.top = start_y
    # F2
    cmd_F2 = FONT.render("F2: take a snapshot", True, WHITE)
    cmd_F2_rect = cmd_space.get_rect()
    cmd_F2_rect.left = left_anchor
    start_y += sep
    cmd_F2_rect.top = start_y
    # F3
    cmd_F3 = FONT.render("F3: enable/disable recording", True, WHITE)
    cmd_F3_rect = cmd_space.get_rect()
    cmd_F3_rect.left = left_anchor
    start_y += sep
    cmd_F3_rect.top = start_y
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
    screen.blit(cmd_F1, cmd_F1_rect)
    screen.blit(cmd_F2, cmd_F2_rect)
    screen.blit(cmd_F3, cmd_F3_rect)
    screen.blit(cmd_p, cmd_p_rect)
    screen.blit(cmd_lr_click, cmd_lr_click_rect)
    screen.blit(cmd_shift_lr_click, cmd_shift_lr_click_rect)


if __name__ == "__main__":
    main()