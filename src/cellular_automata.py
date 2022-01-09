import math
import numpy as np
from constants import *
from patterns import set_glider, set_Gosper_glider_gun

pygame.init()

class CellularAutomata(pygame.sprite.Sprite):
    def __init__(self, configuration=GLIDER):
        """ 
        TODO
        """

        self.configuration = configuration
        self.cells = np.zeros((N_ROW, N_COL))
        self.models = [
            # set_Gosper_glider_gun(8, 5)
        ]
        self.set_initial_state()


    def set_initial_state(self):
        """
        TODO
        """
        for model in self.models:
            for r in range(N_ROW):
                for c in range(N_COL):
                    if (r, c) in model:
                        self.cells[r,c] = 1

    def display_grid(self, screen):
        """
        TODO
        """
        screen.fill(BACKGROUND)
        for r in range(N_ROW):
            y = r * CELL_SIZE
            for c in range(N_COL):
                x = c * CELL_SIZE
                if self.cells[r,c] == 1:
                    cell = ALIVE_CELL
                else:
                    cell = DEAD_CELL
                screen.blit(cell, (x, y))

    def apply_rules(self, environment="Moore"):
        """TODO
        A dictionnary is used to keep track of the cells that will change state
        Rules reminder:
        1. A living cell with fewer than 2 living neighbours dies
        2. A living cell with 2 or 3 living neighbours stays alive
        3. A living cell with more than 3 living cell dies (overpopulation)
        4. A dead cell with exactly 3 living cells becomes alive
        """
        cells_2_change = dict()
        for r in range(N_ROW):
            for c in range(N_COL):
                current_cell = self.cells[r,c]
                alive_neighbors = self.get_alive_neighbors(r, c)
                if current_cell == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        cells_2_change[(r,c)] = 0
                else:
                    if alive_neighbors == 3:
                        cells_2_change[(r,c)] = 1 
        
        for (r, c), cell in cells_2_change.items():
            self.cells[r,c] = cell

    def get_alive_neighbors(self, r, c, environment="Moore") -> int:
        """
        TODO
        """
        pass
        N = N_COL
        alive_neighbors = (
            self.cells[r, (c - 1) % N_COL] +
            self.cells[r, (c + 1) % N_COL] +
            self.cells[(r - 1) % N_ROW, c] +
            self.cells[(r + 1) % N_ROW, c]
        )
        if environment == "Moore":
            alive_neighbors += (
                self.cells[(r - 1) % N_ROW, (c - 1) % N_COL] +
                self.cells[(r + 1) % N_ROW, (c - 1) % N_COL] +
                self.cells[(r + 1) % N_ROW, (c + 1) % N_COL] +
                self.cells[(r - 1) % N_ROW, (c + 1) % N_COL] 
            )
        return alive_neighbors

if __name__ == '__main__':
    pass
