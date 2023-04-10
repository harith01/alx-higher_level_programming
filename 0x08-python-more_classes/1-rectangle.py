#!/usr/bin/python3

"""Defines a Rectangle"""


class Rectangle:
    """Creates a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes an instance of a Rectangle

        Args:
            width (int): Width of the new rectangle
            height (int): height of the new rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of an instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter for an instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the width of an instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Width setter for an instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
