"""TODO"""

# Glider
def set_glider(r, c, grid):
    """Initializes a glider"""
    return (
        (r, c),
        (r - 2, c + 1),
        (r, c + 1),
        (r - 1, c + 2),
        (r, c + 2),
    )

# Gosper's glider gun
def set_Gosper_glider_gun(r, c, grid):
    return (
        (r, c),
        (r, c + 1),
        (r + 1, c),
        (r + 1, c + 1),
        (r, c + 10),
        (r + 1, c + 10),
        (r + 2, c + 10),
        (r - 1, c + 11),
        (r - 2, c + 12),
        (r - 2, c + 13), 
        (r - 1, c + 15),
        (r, c + 16),
        (r + 1, c + 16),
        (r + 2, c + 16),
        (r + 3, c + 15),
        (r + 1, c + 14),
        (r + 1, c + 17),
        (r, c + 20),
        (r - 1, c + 20),
        (r - 2, c + 20),
        (r, c + 21),
        (r - 1, c + 21),
        (r - 2, c + 21),
        (r - 3, c + 22),
        (r - 3, c + 24),
        (r - 4, c + 24),
        (r + 1, c + 22),
        (r + 1, c + 24),
        (r + 2, c + 24),
        (r - 1, c + 34),
        (r - 2, c + 34),
        (r - 1, c + 35),
        (r - 2, c + 35),
        (r + 3, c + 11),
        (r + 4, c + 12),
        (r + 4, c + 13),
    )

