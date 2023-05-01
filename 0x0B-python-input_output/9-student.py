#!/usr/bin/env bash
"""Defines a Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize an Instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of an instance"""

        return self.__dict__
