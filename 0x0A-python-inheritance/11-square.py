#!/usr/bin/python3
"""Square class module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """initialize square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """string representation of the rectangle"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
