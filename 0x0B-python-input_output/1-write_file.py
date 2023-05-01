#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string a text file"""

    with open(filename, 'w', encoding="utf-8") as f:
        n = f.write(text)
    return (n)
