from .add_random_tile import add_random_tile
from .movements import move_left, move_right, move_up, move_down
from .movements import sum

random_variable = 1

single_cc_movements = 0
p1_cc_movements = 0
p2_cc_movements = 0

def move(grid, direction, base, nameUser, modality):

    global sum
    global random_variable
    global single_cc_movements
    global p1_cc_movements
    global p2_cc_movements

    moved = False
    sum = sum
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
    
    cc_movements = 0

    if moved == True:
        if modality == "1":
            single_cc_movements += 1
            cc_movements = single_cc_movements

        if modality == "2":
            
            if random_variable % 2 == 0:
                p2_cc_movements += 1
                cc_movements = p2_cc_movements
            
            else:
                p1_cc_movements += 1
                cc_movements = p1_cc_movements


    return grid, sum, cc_movements


def movements_reseter():
    global single_cc_movements
    global p1_cc_movements
    global p2_cc_movements

    single_cc_movements = 0
    p1_cc_movements = 0
    p2_cc_movements = 0
    
