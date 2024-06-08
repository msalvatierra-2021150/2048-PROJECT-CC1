from .add_random_tile import add_random_tile



# Función que genera el tablero del juego.
def initialize_grid(base, modality):



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