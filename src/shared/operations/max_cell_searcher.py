def max_cell_searcher (grid):
    max_cell=[]

    for rows in grid:
        for cells in rows:
            max_cell.append(cells)
    
    return max(max_cell)