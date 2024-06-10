def board_formatter(grid, sum, movements=0):
    max_cell = []
    emptySpaces = 0
    print("-------------------------")
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell ==  0:
                cell = " "
                emptySpaces+= 1
            print(f" {cell:^3} |", end="")
        print("\n-------------------------")
    for rows in grid:
        for cells in rows:
            max_cell.append(cells)
    print("Cantidad de casillas vacías:", emptySpaces)
    print("Puntaje actual:", sum)
    print("Cantidad de movimientos:", movements)
    print("Número mayor obtenido actualmente:", max(max_cell))