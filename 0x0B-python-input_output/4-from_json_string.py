#!/usr/bin/python3
"""from json to str representation module"""
import json


def from_json_string(my_obj):
    """returns a string from a JSON object"""
    return (json.loads(my_obj))
