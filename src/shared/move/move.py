from ..operations.add_random_tile import add_random_tile
from .movements import move_left, move_right, move_up, move_down, points, sum

random_variable = 1
single_cc_movements = 0
p1_cc_movements = 0
p2_cc_movements = 0

def move(grid, direction, base, nameUser, modality, print_index):
    global points, random_variable, single_cc_movements, p1_cc_movements, p2_cc_movements, sum

    moved = False
    points = points
    sum = sum

    if print_index == 1:
        movement_print(direction, nameUser)
 
    if direction == 'w':
        moved, sum, points = move_up(grid, print_index)
    elif direction == 's':
        moved, sum, points = move_down(grid, print_index)
    elif direction == 'a':
        moved, sum, points = move_left(grid, print_index)
    elif direction == 'd':
        moved, sum, points = move_right(grid, print_index)
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


    return grid, sum, points, cc_movements


def movements_reseter():
    global single_cc_movements, p1_cc_movements, p2_cc_movements

    single_cc_movements = 0
    p1_cc_movements = 0
    p2_cc_movements = 0
    
def movement_print(direction, nameUser):
    if direction == 'w':
        print("\n", nameUser, "se movió hacia arriba \n")
    elif direction == 's':
        print("\n", nameUser, "se movió hacia abajo \n")
    elif direction == 'a':
        print("\n", nameUser, "se movió hacia la izquierda \n")
    elif direction == 'd':
        print("\n", nameUser, "se movió hacia la derecha \n")