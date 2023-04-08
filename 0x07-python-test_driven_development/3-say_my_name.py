#!/usr/bin/python3

"""This defines a function that prints 'My name'"""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name

    Args:
        first_name (str): The first name
	last_name (str): The ;ast name

    Returns:
        My name is <first_name> <last_name>

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
