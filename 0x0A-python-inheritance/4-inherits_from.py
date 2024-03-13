#!/usr/bin/python3
"""Is only exactly sub-class module"""


def inherits_from(obj, a_class):
    """Returns true if an object is an instance
       exactly a subclass, otherwise false"""
    return (issubclass(type(obj), a_class) and (type(obj) is not a_class))
