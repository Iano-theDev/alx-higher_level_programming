#!/usr/bin/python3
"""Is same class module"""


def is_same_class(obj, a_class):
    """Returns true if an object is exactly an instance
       the specified class, otherwise false"""
    return (type(obj) == a_class)
