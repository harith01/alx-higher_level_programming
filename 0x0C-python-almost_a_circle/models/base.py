#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """Defines the "base" class for all
    other classes in this package.

    Private Class Attributes:
    __nb_object (int): Number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
