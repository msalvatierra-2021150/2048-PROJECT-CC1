def board_formatter(grid, sum):
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
    print("Cantidad de casillas vacías:", emptySpaces)
    print("Puntaje actual:", sum)