#!/usr/bin/python3

"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): A list of lists of ints and floats
        div (int/float): The divisor
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different lenghts
        TypeError: If div is not and int or float
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix whose elements are results of division
        of matrix by div
    """

    if (not isinstance(matrix, list) or not
            all(isinstance(row, list) for row in matrix) or not
            all(isinstance(el, (int, float)) for
                row in matrix for el in row)):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda z: round(z / div, 2), row)) for row in matrix]
