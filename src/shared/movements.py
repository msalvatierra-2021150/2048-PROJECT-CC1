def transpose(grid):
    # Devuelve un nuevo grid donde la las columnas pasan a ser filas y las filas a ser columnas.
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    moved = False
    # Ciclo fila por fila de la matriz.
    for row in grid:

        # Arreglo de tiles que no sean ceros.
        row_tiles = [tile for tile in row if tile != 0]

        # Recorre la el arreglo de tiles.
        for i in range(len(row_tiles) - 1):

            # Si en una posición[x] hay una que le siga [x+1] entonces
            # multiplicaremos *2 por tratarse del mismo número.
            # La posición [x] tendrá el resultado del producto
            # La posición [x+1] tendrá un 0.

            if row_tiles[i] == row_tiles[i + 1]:
                row_tiles[i] *= 2
                row_tiles[i + 1] = 0
                moved = True

        # Arreglo de tiles que no sean ceros.
        row_tiles = [tile for tile in row_tiles if tile != 0]

        # Actualización de la fila con las tiles != 0 y un rellenado de 0 para len(row) = 4.
        row[:] = row_tiles + ( [0] * (4 - len(row_tiles)))
        if row_tiles != row:
            moved = True
    return moved

# La lógica se mantiene igual, se hace un revés el grid.
def move_right(grid):
    grid[:] = [row[::-1] for row in grid]
    moved = move_left(grid)
    grid[:] = [row[::-1] for row in grid]
    return moved

# La lógica se mantiene igual, se transpone el grid.
def move_up(grid):
    grid[:] = transpose(grid)
    moved = move_left(grid)
    grid[:] = transpose(grid)
    return moved

# La lógica se mantiene igual, se transpone y se hace un revés el grid.
def move_down(grid):
    grid[:] = transpose(grid)
    grid[:] = [row[::-1] for row in grid]
    moved = move_left(grid)
    grid[:] = [row[::-1] for row in grid]
    grid[:] = transpose(grid)
    return moved