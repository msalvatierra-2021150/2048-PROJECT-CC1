from .movements import sum
from .move import move
import copy

def machine_algorithm(machine_board, base, nameUser):
    global sum
    directions = ['w', 's', 'a', 'd']
    sums = {}

    for direction in directions:
        sum = 0
        # Pass a deep copy of machine_board to ensure it is not mutated
        result = move(grid=copy.deepcopy(machine_board), direction=direction, nameUser=nameUser, modality="1", base=base)[1]
        sums[direction] = result

    # Find the direction with the greatest sum
    best_direction = max(sums, key=sums.get)
    sum = 0  # Reset the global sum to zero

    return best_direction