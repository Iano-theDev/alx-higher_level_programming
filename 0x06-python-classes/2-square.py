#!/usr/bin/python3
''' Defining a square Class'''


class Square:
    """Represents a square

    Attributes:
    __size(int): size of a side of the square
    """
    def __init__(self, __size=0):
        """Initializes the square class
        Args:
        size(int): size of a side of the square

        Return:
        None
        """
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
