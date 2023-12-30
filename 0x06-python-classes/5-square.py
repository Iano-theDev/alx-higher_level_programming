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

    def my_print(self):
        """Prints a square using # """
        if self.__size == 0:
            print()
        for n in range(self.__size):
            print("".join(["#" for n in range(self.__size)]))
        print()
