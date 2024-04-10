#!/usr/bin/python3
"""Rectangle class module"""
from models import base

Base = base.Base


class Rectangle(Base):
    """Representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A getter for the private instance attribute width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """A getter for the private instance attribute x(latitude position)"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for lattitude position of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """A getter for the private instance attribute y (logitude position)"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for longitude position of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle isntance"""
        return (self.__width * self.__height)