import random

class CellularAutomata():
    def __init__(self, nb_col=20, nb_row=20):
        """ Constructor
        """
        self.nb_col, self.nb_row = nb_col, nb_row
        self.grid = [[' ' for _ in range(self.nb_col)] for _ in range(self.nb_row)]
        
        self.set_initial_state()

    def __str__(self):
        """ Display the full CA grid
        Parameters:
            None
        Returns:
            type string: the grid as a string
        """
        display_grid = f'{"-" * 2*self.nb_col}'
        for row in self.grid:
            display_grid += f'{" ".join(row)}' + '\n'
        display_grid += f'{"-" * 2* self.nb_col}'

        return display_grid

    def set_initial_state(self):
        # Glider
        self.grid[10][10] = '*' 
        self.grid[11][10] = '*'
        self.grid[9][10] = '*'
        self.grid[11][9] = '*'
        self.grid[10][8] = '*'


    def get_alive_neighbours(self, r, c, environment='Moore'):
        """ Get the number of alive alive neighbours on a given cell
        Parameters:
            r: int (the row index of the local cell)
            c: int (the column index of the local cell)
            environement: string (environement's type) [optional, default='Moore']
        Returns:
            type int: number of alive neighbours
        """
        alive_neighbours = 0
        for row in range(max(0, r-1), min(r+1, self.nb_row-1)+1):
            for col in range(max(0, c-1), min(c+1, self.nb_col-1)+1):
                if row == r and col == c:
                    continue
                if self.grid[row][col] == '*':
                    alive_neighbours += 1
        return alive_neighbours


    def apply_rules(self):
        """ Apply the rules of the game of life
        A dictionnary is used to keep track of the cells that will change state
        Rules reminder:
        1. A living cell with fewer than 2 living neighbours dies
        2. A living cell with 2 or 3 living neighbours stays alive
        3. A living cell with more than 3 living cell dies (overpopulation)
        4. A dead cell with exactly 3 living cells becomes alive
        Parameters:
            None
        Returns:
            None
        """
        cells_2_change = dict() 

        for row in range(self.nb_row):
            for col in range(self.nb_col):
                alive_neighbours = self.get_alive_neighbours(row, col)
                # Current cell is alive
                if self.grid[row][col] == '*':
                    if alive_neighbours in (2, 3): # The cell stays alive
                        continue
                    # Rules 1 and 3 
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        cells_2_change[(row, col)] = ' ' # The cell dies 
                # Current cell is dead
                else:
                    # Rules 4
                    if alive_neighbours == 3:
                        cells_2_change[(row, col)] = '*' # The cell becomes alive

        for key in cells_2_change.keys():
            r, c = key
            self.grid[r][c] = cells_2_change[key]

if __name__ == '__main__':
    CA = CellularAutomata()
    print(CA)
    for i in range(40):
        CA.apply_rules()
        print(CA)

