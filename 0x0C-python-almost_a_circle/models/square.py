#!/usr/bin/python3
"""The square class module"""
from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns a printable string representation of a square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """getter for the size(width and height of the square)"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size(width and height) of the square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
