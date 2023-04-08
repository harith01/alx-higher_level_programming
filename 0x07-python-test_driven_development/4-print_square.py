#!/usr/bin/python3

"""This is a module that prints a square of #"""


def print_square(size):
    """Prints square with character #
    
    Args:
    size (int): size of the square

    Raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    TypeError: If size is a float and is less than 0

    Returns:
    A square with the character #

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
