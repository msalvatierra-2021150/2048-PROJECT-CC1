from .add_random_tile import add_random_tile
import copy

copy_of_grid = "Aquí se copiará el tablero"
turn_indicator_for_grid = 2

# Función que genera el tablero del juego.
def initialize_grid(base, modality):

    global copy_of_grid
    global turn_indicator_for_grid

    #Caso único para tablero de jugador individual.
    if modality == "1":
        #Matriz (Tablero)
        grid = [
            # Genera una fila
            [0 for _ in range(4)]

            # Repite la creación de las filas 4 veces.
            for _ in range(4)
        ]

        add_random_tile(grid, base)
        add_random_tile(grid, base)
        

        return grid
    
    #Caso para copiar tablero en multijugador
    if modality in ["2", "3"]:

        if turn_indicator_for_grid == 2:
            turn_indicator_for_grid -= 1
            #Matriz (Tablero)
            grid = [
                # Genera una fila
                [0 for _ in range(4)]

                # Repite la creación de las filas 4 veces.
                for _ in range(4)
            ]

            add_random_tile(grid, base)
            add_random_tile(grid, base)
            
            actual_grid = grid
            copy_of_grid = copy.deepcopy(actual_grid)
            
        

        elif turn_indicator_for_grid == 1:
            turn_indicator_for_grid += 1
            actual_grid = copy_of_grid

        
        return actual_grid