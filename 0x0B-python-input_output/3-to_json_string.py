#!/usr/bin/python3
"""JSON representation module"""
import json


def to_json_string(my_obj):
    """returns a json representation of a string"""
    return (json.dumps(my_obj))
