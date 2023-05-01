#!/usr/bin/python3
"""Defines a function that writes an object
to a file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON representation"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
