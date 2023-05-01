#!/usr/bin/python3
# Defines a function that return the dictionary description 
# with simple data structure for JSON serialization of an object


def class_to_json(obj):
    """Returns the dictionary description of an
    object in JSON"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
