#!/usr/bin/python3
"""Defines a Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize an Instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of an instance"""

        obj = self.__dict__

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return obj
            d = {}
            for attr in attrs:
                for obj_attr in obj:
                    if attr == obj_attr:
                        d[attr] = obj[obj_attr]
            return d
        return obj

    def reload_from_json(self, json):
        """Replaces all attributes of an instance of Student"""

        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
