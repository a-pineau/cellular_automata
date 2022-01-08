import sys
import math
import random
import pygame
from pygame import gfxdraw
from pygame.locals import *
from constants import *
from ordered_set import OrderedSet
from copy import deepcopy

pygame.init()

class CellularAutomata(pygame.sprite.Sprite):
    def __init__(self, configuration=TEST):
        """ 
        TODO
        """

        self.configuration = configuration
        self.cells_position = dict()
        self.cells_2_change = dict()
        self.set_initial_state()

    def set_initial_state(self):
        """
        TODO
        """
        y = 0
        for i in range(NB_X):
            x = 0
            for j in range(NB_Y):
                if (x, y) in self.configuration:
                    self.cells_position[(x, y)] = ALIVE_CELL
                else:
                    self.cells_position[(x, y)] = DEAD_CELL
                x += CELL_SIZE
            y += CELL_SIZE

    def display_grid(self, screen):
        """
        TODO
        """
        screen.fill(BACKGROUND)
        for pos, cell in self.cells_position.items():
            screen.blit(cell, pos)

    def apply_transition_rules(self, environment="Moore"):
        """TODO
        A dictionnary is used to keep track of the cells that will change state
        Rules reminder:
        1. A living cell with fewer than 2 living neighbours dies
        2. A living cell with 2 or 3 living neighbours stays alive
        3. A living cell with more than 3 living cell dies (overpopulation)
        4. A dead cell with exactly 3 living cells becomes alive
        """
        for pos, cell in self.cells_position.items():
            r, c = pos
            alive_neighbors = self.get_alive_neighbors(r, c)
            if cell == ALIVE_CELL:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    self.cells_2_change[pos] = DEAD_CELL
            else:
                if alive_neighbors == 3:
                    self.cells_2_change[pos] = ALIVE_CELL 

        # Updating grid
        for new_pos, cell in self.cells_2_change.items():
            self.cells_position[new_pos] = cell

    def apply_transition_rules_2(self, environment="Moore"):
        """TODO
        A dictionnary is used to keep track of the cells that will change state
        Rules reminder:
        1. A living cell with fewer than 2 living neighbours dies
        2. A living cell with 2 or 3 living neighbours stays alive
        3. A living cell with more than 3 living cell dies (overpopulation)
        4. A dead cell with exactly 3 living cells becomes alive
        """
        for pos, cell in self.cells_position.items():
            r, c = pos
            alive_neighbors = self.get_alive_neighbors(r, c)
            if alive_neighbors < 4:
                self.cells_2_change[pos] = DEAD_CELL
            elif alive_neighbors >= 5:
                self.cells_2_change[pos] = ALIVE_CELL
  
        # Updating grid
        for new_pos, cell in self.cells_2_change.items():
            self.cells_position[new_pos] = cell

    # SEE BOOK (RETURN GENERATOR INSTEAD OF LIST)
    def get_alive_neighbors(self, r, c, environment="Moore") -> list:
        """
        TODO
        """
        alive_neighbors = 0
        neighbors = [
            (r, c - CELL_SIZE),
            (r, c + CELL_SIZE),
            (r - CELL_SIZE, c),
            (r + CELL_SIZE, c),
        ]
        if environment == "Moore":
            neighbors.extend([
                (r - CELL_SIZE, c - CELL_SIZE),
                (r - CELL_SIZE, c + CELL_SIZE),
                (r + CELL_SIZE, c - CELL_SIZE),
                (r + CELL_SIZE, c + CELL_SIZE),
            ])
        for n in neighbors:
            try:
                self.cells_position[n]
            except KeyError:
                continue
            else:
                if self.cells_position[n] == ALIVE_CELL:
                    alive_neighbors += 1
        return alive_neighbors


if __name__ == '__main__':
    CA = CellularAutomata()
    CA.set_initial_state()
    CA.apply_transition_rules()
