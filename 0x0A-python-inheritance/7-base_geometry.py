#!/usr/bin/python3
"""Base geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an value passed to it"""
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
