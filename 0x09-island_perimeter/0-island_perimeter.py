#!/usr/bin/python3
"""
Island Perimeter Challenge"
"""

def island_perimeter(grid):
    """
    Calculates the perimetr of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    x = 0
    for m in range(len(grid)):
        for n in range(len(grid)):
            if (grid[m][n] == 1):
                if (m <= 0 or grid[m - 1][n] == 0):
                    x += 1
                if (m >= len(grid) - 1 or grid[m + 1][n] == 0):
                    x += 1
                if (n <= 0 or grid[m][n - 1] == 0):
                    x += 1
                if (n >= len(grid[m]) - 1 or grid[m][n + 1] == 0):
                    x += 1
    return x

