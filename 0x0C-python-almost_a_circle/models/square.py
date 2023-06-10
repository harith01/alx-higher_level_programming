#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of Square

        Args:
            size (int): The size of the square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The ID of the square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override __str___"""

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """Set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and height to size"""
        self.width = value
        self.height = value
