#!/usr/bin/python3
"""
Addition module
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result
    
    Parameters:
    a (int): first integer
    b (int): second integer

    Return:
    int: Sum of a and b
    """
    if type(a) is not int or type(b) is not float:
        raise TypeError("a must be an integer")
    else if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
