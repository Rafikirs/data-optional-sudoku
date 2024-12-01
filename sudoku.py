# pylint: disable=missing-docstring

def sudoku_validator(grid):
    for i in range(9):
        if sorted([grid[i][j] for j in range(9)]) != list(range(1, 10)):
            return False

    for j in range(9):
        if sorted([grid[i][j] for i in range(9)]) != list(range(1, 10)):
            return False

    for k in range(3):
        for h in range(3):
            if sorted([grid[i][j] for i in range(3*k, 3*k+3)
                for j in range(3*h, 3*h+3)]) != list(range(1, 10)):
                return False

    return True
