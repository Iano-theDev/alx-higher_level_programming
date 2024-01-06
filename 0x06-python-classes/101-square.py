#!/usr/bin/python3
'''Defines a square class'''


class Square:
    """Representation of a square
    Attributes:
    __size(int): size of a side of the square
    __position(tuple): a tuple of 2 positive integers
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square class
        Args:
        size(int): size of a side of the square
        position(tuple): position of the square

        Return:
            None
        """
        self.size = size
        self.position = position

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
            return
        for lat in range(self.__position[1]):
            print()
        for n in range(self.__size):
            print("".join([" " for lon in range(self.__position[0])]), end="")
            print("".join(["#" for n in range(self.__size)]))

    @property
    def position(self):
        """Getter for the position attribute
        Return:
            position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the poistion
        Args:
            value(tuple): A tuple of two positive ints

        Return:
            Null"""
        if len(value) != 2\
           or type(value[0]) is not int\
           or type(value[1]) is not int\
           or value[0] < 0\
           or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """Returns a printable string value for a square instance
        """
        my_square = ""
        if self.my_print() is not None:
            my_square += self.my_print
        return str(my_square)
