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

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns string when print()"""

        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
