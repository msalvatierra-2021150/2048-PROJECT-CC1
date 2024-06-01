def board_formatter(grid):
    print("-------------------------")
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell:^3} |", end="")
        print("\n-------------------------")