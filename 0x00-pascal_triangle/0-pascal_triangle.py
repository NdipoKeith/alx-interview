#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a
   list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    pas = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = pas[row_number - 1][j - 1] + pas[row_number - 1][j]
            row.append(element)
        row.append(1)
        pas.append(row)

    return pas
