#!/usr/bin/python3
"""Defines a functionthat checks the class of an instance"""


def is_kind_of_class(obj, a_class):
    """Check if an Object is an Instance of a Class

    Args:
        obj (any): the object
        a_class (any): the class

    Returns:
        True - If it matches
        False - Otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
