#!/usr/bin/python3
"""The say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Prints the full name of a person

    Args:
        first_name (string): The first name
        last_name (string): The last name, default is empty string

    Return:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
