#!/usr/bin/python3
"""The Base class module"""


class Base:
    """Representation of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
