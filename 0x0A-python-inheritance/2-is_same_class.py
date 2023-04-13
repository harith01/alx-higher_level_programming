#!/usr/bin/python3
"""Module that determines if an object is an instance
of the specified class"""


def is_same_class(obj, a_class):
    """Function that determines if an object is
    an instance of the specified class

    Args:
        obj (any): The object
        a_class (type): The class

    Returns:
        True- if obj is exactly an instance
        False- Otherwise
    """

    if type(obj) == a_class:
        return True
    False
