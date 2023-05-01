#!/usr/bin/python3
"""A module that contains a function
that reads a text file
"""


def read_file(filename=""):
    """Defines a function that reads a text file"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
