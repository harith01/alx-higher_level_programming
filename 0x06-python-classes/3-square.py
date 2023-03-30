#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square

    Args:
        size (int): size of square

    Attributes:
        size (int): size of square

    """

    def __init__(self, size=0):
        """Initializes an instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of square"""

        return self.__size * self.__size
