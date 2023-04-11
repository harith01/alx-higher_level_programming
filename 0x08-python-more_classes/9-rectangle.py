#!/usr/bin/python3

"""Defines a Rectangle"""


class Rectangle:
    """Creates a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes an instance of a Rectangle

        Args:
            width (int): Width of the new rectangle
            height (int): height of the new rectangle

        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """Returns the area of a rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle with # character"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Prints a representation of the Object"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete an instance of a Class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines the bigger rectangle

        Args:
        rect_1 (Rectangle): first rectangle
        rect_2 (Rectangle): second rectangle

        Returns:
        rect_1: if both have the same area
        Or The bigger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a Square using Rectangle Class"""

        return cls(size, size)