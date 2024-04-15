#!/usr/bin/python3
"""The square class module"""
from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a printable string representation of a square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
