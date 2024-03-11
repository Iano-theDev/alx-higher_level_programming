#!/usr/bin/python3
"""Object lookup module"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)
