#!/usr/bin/python3

"""This is a module for add_integr"""

def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The addition of a and b

    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
