#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                
                # If there's a land cell above, subtract 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                
                # If there's a land cell to the left, subtract 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    
    return perimeter
