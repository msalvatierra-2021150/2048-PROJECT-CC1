sum = 0

def transpose(grid):
    # Devuelve un nuevo grid donde la las columnas pasan a ser filas y las filas a ser columnas.
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    global sum
    moved = False
    for row in grid:
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                sum += row[i]
                row[i + 1] = 0

    # Ciclo fila por fila de la matriz.
    for row in grid:
        # Arreglo de tiles que no sean ceros.
        row_tiles = [tile for tile in row if tile != 0]
        # Actualización de la fila con las tiles != 0 y un rellenado de 0 para len(row) = 4.
        row[:] = row_tiles + [0] * (4 - len(row_tiles))
        moved = True
    return moved, sum

def move_right(grid):
    grid[:] = [row[::-1] for row in grid]
    moved, sum = move_left(grid)
    grid[:] = [row[::-1] for row in grid]
    return moved, sum

def move_up(grid):
    grid[:] = transpose(grid)
    moved, sum = move_left(grid)
    grid[:] = transpose(grid)
    return moved, sum

def move_down(grid):
    grid[:] = transpose(grid)
    grid[:] = [row[::-1] for row in grid]
    moved, sum = move_left(grid)
    grid[:] = [row[::-1] for row in grid]
    grid[:] = transpose(grid)
    return moved, sum


def score_reseter():
    global sum
    sum = 0