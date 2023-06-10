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

    def update(self, *args, **kwargs):
        """Update the class Square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
