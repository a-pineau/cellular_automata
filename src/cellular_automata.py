import math
import numpy as np
import pygame

from constants import *
from patterns import set_glider, set_Gosper_glider_gun

pygame.init()

class CellularAutomata(pygame.sprite.Sprite):
    """
    A class used to represent a standard 2D Cellular Automata (CA) grid.
    The CA grid evolves according to the Conway's Game of Life standard
    transition rules (see apply_rules() method).
    The grid is a N_ROW * N_COL rectangle filled with square cells (CELL_SIZE * CELL_SIZE).
    The default neighborhood used is the Moore environment (8 nearest neighbors).
    
    Attributes
    ----------
    cells: numpy.ndarray
        2D array representing the CA grid
    cells_rect: list
        list of pygame.Rect objects used to display the grid onscreen

    Methods
    -------
    display_grid(self, screen) -> None
        Display (using Pygame) the current grid onscreen.
    change_cell_state(self, click, pressed) -> None
        Change the state of a current cell when clicking on it w/ the mouse
    reset_grid(self) -> None
        Fill the grid with zeros (kill all cells alive)
    apply_rules(self) -> None
        Apply the standard Game of Life transition rules to the current grid
    get_alive_neighbors(self, environment="Moore") -> int
        Return the number of neighbors alive of a given cell
    """

    # Constructor
    # -----------
    def __init__(self):
        """Constructor. Initializes the grid."""
        self.cells = np.zeros((N_ROW, N_COL))
        
    # Methods
    # -----------
    def change_cell_state(self, click=None, pressed=None) -> None:
        """Change the state of a given cell.

        Left clicking on a dead cell gives birth to it.
        Right clicking on a living cell kills it.
        Holindg shift + left clicking on mulitple dead cells gives them birth.
        Holding shift + right clicking on multiple living cells kills them.

        Parameter
        ---------
        click: bool (keyword argument)
            True if any button of the mouse is being clicked on, False otherwise.
        pressed: bool (keyword argument)
            True if any button of the mouse is being pressed, False otherwise.
        """

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

    def get_grid(self) -> np.ndarray:
        """Returns the current grid"""
        return self.cells

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
        """RReturns the number of neighbors alive of a given cell.

        A toroidal surface is considered, e.g. the left neighbor of a left border
        cell corresponds to its right counterpart (i.e. the right border cell).

        Parameters
        ----------
        r: int (required)
            Row index of the current cell
        c: int (required)
            Col index of the current cell
        environment: string (optional, default="Moore")
            When using a Moore environment, the 8 nearest neighbors of a given
            cell are considered. Otherwise (von Neumann environment), the 4
            nearest neighbors are considered.

        Returns
        -------
        int
            Number of alive neighbors
        """

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
    CA = CellularAutomata()


if __name__ == '__main__':
    main()
