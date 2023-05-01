#!/usr/bin/python3
"""Defines a function that appends to a file"""


def append_write(filename="", text=""):
    """Appends a string to a text file"""

    with open(filename, 'a', encoding="utf-8") as f:
        nb = f.write(text)
    return (nb)
