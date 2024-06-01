from .add_random_tile import add_random_tile
from .movements import move_left, move_right, move_up, move_down

def move(grid, direction):
    moved = False
    if direction == 'w':
        moved = move_up(grid)
    elif direction == 's':
        moved = move_down(grid)
    elif direction == 'a':
        moved = move_left(grid)
    elif direction == 'd':
        moved = move_right(grid)
    if moved:
        add_random_tile(grid)
    return grid