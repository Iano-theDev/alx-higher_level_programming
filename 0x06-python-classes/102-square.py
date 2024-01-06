#!/usr/bin/python3
'''Defines a square class'''


class Square:
    """Representation of a square
    Attributes:
    __size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square class
        Args:
        size(int): size of a side of the square

        Return:
        None
        """
        self.size = size

    @property
    def size(self):
        """Getter of __size

        Return:
        the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
        value(int): value to set size

        Return:
        None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Gives the area of a square

        Return:
        Area of the square
        """
        return (self.__size * self.__size)

    def __lt__(self, other):
        """Compares if a square instance's area is less than
        another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's less than"""
        return self.size < other.size

    def __le__(self, other):
        """Compares if a square instance's area is less than
        or equal to another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's less than or equal to"""
        return self.size <= other.size

    def __ne__(self, other):
        """Compares if a square instance's area is not
        equal to another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's not equal to"""
        return self.size != other.size

    def __gt__(self, other):
        """Compares if a square instance's area is greater than
        another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's greater than"""
        return self.size > other.size

    def __ge__(self, other):
        """Compares if a square instance's area is greater than
            or equal to another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's greater than or equal to"""
        return self.size >= other.size

    def __eq__(self, other):
        """Compares if a square instance's area is
            equal to another square instance
        Args:
            other(Square): square to be compared with
        Return:
            boolean: true if area's equal to"""
        return self.size == other.size
