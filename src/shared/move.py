from .add_random_tile import add_random_tile
from .movements import move_left, move_right, move_up, move_down

def move(grid, direction, base, nameUser):
    moved = False
    sum = 0  # Initialize sum to avoid reference before assignment
    if direction == 'w' or direction == 'W':
        print("\n", nameUser, "se movió hacia arriba \n")
        moved, sum = move_up(grid)
    elif direction == 's' or direction == 'S':
        print("\n", nameUser, "se movió hacia abajo \n")
        moved, sum = move_down(grid)
    elif direction == 'a' or direction == 'A':
        print("\n", nameUser, "se movió hacia la izquierda \n")
        moved, sum = move_left(grid)
    elif direction == 'd' or direction == 'D':
        print("\n", nameUser, "se movió hacia la derecha \n")
        moved, sum = move_right(grid)
    if moved:
        add_random_tile(grid, base)
    return grid, sum
