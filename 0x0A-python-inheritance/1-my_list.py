#!/usr/bin/python3
"""MyList class Module"""


class MyList(list):
    """Inherits from list"""
    def __init__(self):
        """Initialize object instacne"""
        super().__init__()

    def print_sorted(self):
        """prints a list in sorted ascending order"""
        print(sorted(self))
