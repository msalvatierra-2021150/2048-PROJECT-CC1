sum = 0
points = 0

def transpose(grid):
    # Devuelve un nuevo grid donde la las columnas pasan a ser filas y las filas a ser columnas.
    return [list(row) for row in zip(*grid)]

def move_board(grid):
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

def move_left(grid, print_index):
    sum_reseter()
    moved, sum = move_board(grid)
    points, sum = score_analisis(sum, print_index)
    return moved, sum, points

def move_right(grid, print_index):
    sum_reseter()
    grid[:] = [row[::-1] for row in grid]
    moved, sum = move_board(grid)
    grid[:] = [row[::-1] for row in grid]
    points, sum = score_analisis(sum, print_index)
    return moved, sum, points

def move_up(grid, print_index):
    sum_reseter()
    grid[:] = transpose(grid)
    moved, sum = move_board(grid)
    grid[:] = transpose(grid)
    points, sum = score_analisis(sum, print_index)
    return moved, sum, points

def move_down(grid, print_index):
    sum_reseter()
    grid[:] = transpose(grid)
    grid[:] = [row[::-1] for row in grid]
    moved, sum = move_board(grid)
    grid[:] = [row[::-1] for row in grid]
    grid[:] = transpose(grid)
    points, sum = score_analisis(sum, print_index)
    return moved, sum, points

def score_reseter():
    global points
    points = 0

def sum_reseter():
    global sum
    sum = 0

def score_analisis(sum_value, print_index):
    global points, sum
    if print_index == 1:
        points += sum_value
        return points, sum
    if print_index == 2:
        sum += points
        return 0, sum
    else:
        return 0