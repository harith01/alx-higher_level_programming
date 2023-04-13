#!/usr/bin/python3
"""Defines a functionthat checks the class of an instance"""


def inherits_from(obj, a_class):
    """Check if an Object inherits from a Class

    Args:
        obj (any): the object
        a_class (any): the class

    Returns:
        True - If it inherits
        False - Otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
