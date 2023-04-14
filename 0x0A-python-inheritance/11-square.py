#!/usr/bin/python3
"""Defines a BaseGeometry Class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size):
        """Initializes an instance of Square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes area of Square"""

        return self.__size * self.__size

    def __str__(self):
        """Prints description of Square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
