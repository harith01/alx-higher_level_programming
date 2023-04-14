#!/usr/bin/python3
"""Defines a BaseGeometry Class"""


class BaseGeometry:
    """Defines a BaseGeometry Class"""

    def area(self):
        """Computes the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an Integer value"""

        if type(value).__name__ != 'int':
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a Rectangle"""

    def __init__(self, width, height):
        """Initializes an instance of Rectangle"""

        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
