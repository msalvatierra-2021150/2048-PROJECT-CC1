from .add_random_tile import add_random_tile
from .movements import move_left, move_right, move_up, move_down

def move(grid, direction, base, nameUser):
    moved = False
    if direction == 'w' or direction == 'W':
        print ("\n", nameUser, "realizo se movio hacia arriba \n")
        moved = move_up(grid)
    elif direction == 's' or direction == 'S':
        print ("\n", nameUser, "realizo se movio hacia abajo \n")
        moved = move_down(grid)
    elif direction == 'a' or direction == 'A':
        print ("\n", nameUser, "realizo se movio hacia la izquierda \n")
        moved = move_left(grid)
    elif direction == 'd' or direction == 'D':
        print ("\n", nameUser, "realizo se movio hacia la derecha \n")
        moved = move_right(grid)
    if moved:
        add_random_tile(grid, base)
    return grid