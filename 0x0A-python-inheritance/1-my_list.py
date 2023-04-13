#!/usr/bin/python3
"""Implements a Class that inherits from List"""


class MyList(list):
    """MyList Class Definition"""

    def __init__(self):
        """Instance initialization"""
        list.__init__(self)

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
