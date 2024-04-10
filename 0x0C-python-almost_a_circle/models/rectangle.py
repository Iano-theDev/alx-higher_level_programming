#!/usr/bin/python3
"""Rectangle class module"""
Base = __import__('base').Base

class Rectangle(Base):
    """Representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle class"""
        super.__init__(id)
        self.width = width
        self.height = height

    @setter.width
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        else:
            self.__width = value

    @property
    def width(self):
        """A getter for the private instance attribute width"""
        return self.__width

    @setter.height
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        else:
            self.__height = value

    @property
    def height:
        """A getter for the private instance attribute width"""
        return self.__height
    
