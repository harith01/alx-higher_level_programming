#!/usr/bin/python3

"""Implements MyInt class that inherits from int"""


class MyInt:
    """Defines MyInt"""

    def __init__(self, value):
        """Initializing Int"""

        self.__value = value

    def __eq__(self, other):
        """Inverts isequal function"""

        if self.__value == other:
            return False
        return True

    def __ne__(self, other):
        """Inverts not-equal function"""

        if self.__value != other:
            return False
        return True

    def __str__(self):
        """Return value to print"""

        return "{}".format(self.__value)
