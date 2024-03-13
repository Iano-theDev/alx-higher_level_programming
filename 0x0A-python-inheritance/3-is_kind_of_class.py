#!/usr/bin/python3
"""Is same class module"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance
       the specified class or of a subclass, otherwise false"""
    return isinstance(obj, a_class)
