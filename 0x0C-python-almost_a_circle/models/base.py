#!/usr/bin/python3
"""The Base class module"""
import json

class Base:
    """Representation of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string repr of list_dictionaries"""
        j_list = []
        if list_dictionaries is None:
            return str(j_list)
        else:
            for item in list_dictionaries:
                j_list.append(json.dumps(item))
            return str(j_list)
