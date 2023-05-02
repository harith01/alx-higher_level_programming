#!/usr/bin/python3
"""Defines a function that generates Pascal's triangle"""


def pascal_triangle(n):
    """Generates a Pascal triangle"""

    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        row = [1]
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])
        row.append(1)
        triangles.append(row)
    return triangles
