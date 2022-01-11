import math
import numpy as np
from constants import *
from patterns import set_glider, set_Gosper_glider_gun

pygame.init()

class CellularAutomata(pygame.sprite.Sprite):
    def __init__(self):
        """ 
        TODO
        """
        self.gen = 0
        self.cells = np.zeros((N_ROW, N_COL))
        self.cells_rect = [pygame.Rect((x * CELL_SIZE, y * CELL_SIZE + Y_OFFSET), 
                           (CELL_SIZE, CELL_SIZE)) for x in range(N_COL) for y in range(N_ROW)]

    def display_grid(self, screen) -> None:
        """
        TODO
        """
        screen.fill(BACKGROUND)
        for r in range(N_ROW):
            y = r * CELL_SIZE + Y_OFFSET
            for c in range(N_COL):
                x = c * CELL_SIZE
                current_cell = self.cells[r, c]
                screen.blit(CELL_IMGS[current_cell], (x, y))

    def change_cell_state(self, click=None, pressed=None) -> None:
            x, y = pygame.mouse.get_pos()
            r = (y - Y_OFFSET) // CELL_SIZE
            c = x // CELL_SIZE
            try:
                self.cells[r, c]
            except IndexError:
                return None
            else:
                if r >= 0 and c >= 0:
                    if (click and click == 1) or (pressed and pressed[0]):
                        self.cells[r, c] = 1
                    elif (click and click == 3) or (pressed and pressed[2]):
                        self.cells[r, c] = 0

    def reset_grid(self) -> None:
        """Fill the grid with dead cells (used when restarting the game)."""
        self.cells = np.zeros((N_ROW, N_COL))

    def get_stats_cells(self) -> tuple:
        """Returns the number of cells alive and the associated percentage."""
        n_alive_cells = np.count_nonzero(self.cells == 1)
        size_grid = N_COL * N_ROW
        percentage_alive = round((n_alive_cells / size_grid) * 100, 2)
        return n_alive_cells, percentage_alive


    def apply_rules(self, environment="Moore") -> None:
        """Apply the (standard) transition rules to the current grid.

        A dictionnary is used to keep track of the cells that will change state
        Rules reminder:
        1. A living cell with fewer than 2 living neighbours dies
        2. A living cell with 2 or 3 living neighbours stays alive
        3. A living cell with more than 3 living cell dies (overpopulation)
        4. A dead cell with exactly 3 living cells becomes alive

        Parameter
        ---------
        environment: string (optional, default="Moore")
            Cellular automata environment (Moore: 8 nearest neighbors)
            Otherwise, a von Neumann environment is used (4 nearest neighbors)
        """

        cells_2_change = dict()
        for r in range(N_ROW):
            for c in range(N_COL):
                current_cell = self.cells[r, c]
                alive_neighbors = self.get_alive_neighbors(r, c)
                if current_cell == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        cells_2_change[(r, c)] = 0
                else:
                    if alive_neighbors == 3:
                        cells_2_change[(r, c)] = 1 
        for (r, c), cell in cells_2_change.items():
            self.cells[r, c] = cell

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


def main():
    pass


if __name__ == '__main__':
    main()
