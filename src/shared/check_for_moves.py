from .movements import transpose

def check_for_moves(grid):
    # Sí hay algún espacio, aún hay movimientos.
    for row in grid:
        for tile in row:
            if tile == 0:
                return True

    # Chequeo por cada posible movimiento.
    if check_for_left_moves(grid):
        return True
    if check_for_right_moves(grid):
        return True
    if check_for_upward_moves(grid):
        return True
    if check_for_downward_moves(grid):
        return True

    # Si nno hay movimientos posibles, return False.
    return False

def check_for_left_moves(grid):
    for i in range(4):
        for j in range(4):
            if (i < 3 and grid[i][j] == grid[i+1][j]) or (j < 3 and grid[i][j] == grid[i][j+1]):
                return True
    return False

def check_for_right_moves(grid):
    grid_reversed = [row[::-1] for row in grid]
    if check_for_left_moves(grid_reversed):
        return True
    return False

def check_for_upward_moves(grid):
    grid_transposed = transpose(grid)
    if check_for_left_moves(grid_transposed):
        return True
    return False

def check_for_downward_moves(grid):
    grid_transposed = transpose(grid)
    grid_reversed = [row[::-1] for row in grid_transposed]
    if check_for_left_moves(grid_reversed):
        return True
    return False
