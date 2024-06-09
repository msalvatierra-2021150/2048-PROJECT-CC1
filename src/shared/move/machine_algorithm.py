from .movements import sum
from .move import move
import copy

condition_counter = 1

def machine_algorithm(machine_board, base, nameUser, old_direction):
    global sum, condition_counter
    directions = ['w', 's', 'a', 'd']
    sums = {}
    for direction in directions:
        sum = 0
        # Pass a deep copy of machine_board to ensure it is not mutated
        result = move(grid=copy.deepcopy(machine_board), direction=direction, base=base, nameUser=nameUser, modality="1", print_index=2)[1]
        sums[direction] = result

    # Find the direction with the greatest sum
    
    best_direction = max(sums, key=sums.get)
    sum = 0  # Reset the global sum to zero
    
    if best_direction in ['w', 'a'] and condition_counter > 2:
        if old_direction == best_direction:
            if best_direction == 'w':
                best_direction = 's'
                condition_counter = 1
            elif best_direction == 'a':
                best_direction = 'd'
                condition_counter = 1
    else:
        condition_counter += 1
    
    return best_direction