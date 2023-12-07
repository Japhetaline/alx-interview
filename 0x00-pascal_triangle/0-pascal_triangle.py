#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            tri.append([1])
        else:
            cur_row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    cur_row.append(1)
                else:
                    cur_row.append(tri[i - 1][j - 1] +
                                   tri[i - 1][j])

            tri.append(cur_row)

    return (tri)
