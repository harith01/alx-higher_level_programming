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
        self.__size = size

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes an instance"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
