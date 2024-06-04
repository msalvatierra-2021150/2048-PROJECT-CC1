import random

# Función para añadir tiles al tablero donde hayan posiciones vacías.
def add_random_tile(grid, base):

    # Arreglo para las coordenadas vacías.
    empty_positions = [
        (x, y)
        # Iterador para el largo de las filas.
        for x in range(4)
            # Iterador para los elementos de cada fila.
            for y in range(4)
                # En caso la posición tenga un 0, se devuelve la coordenada
                if grid[x][y] == 0
    ]

    if empty_positions:
        # Toma una fila y un elemento.
        x, y = random.choice(empty_positions)
        # Devuelve un dos o un cuatro para la tile en esa coordenada
        grid[x][y] = base if random.random() < 0.9 else base * 2
