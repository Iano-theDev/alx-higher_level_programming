#!/usr/bin/python3
"""
Classes:
    Rectangle: Represents a simple rectangle
"""


class Rectangle:
    """Represents a simple rectangle

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns a string representation of the rectangle"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        rect = ("".join(["#" for n in range(self.width)]) + "\n") * self.height
        return rect[:-1]

    def __repr__(self):
        """Returns an officlial string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Detects deletion of a rectangle"""
        print(f'Bye rectangle...')
