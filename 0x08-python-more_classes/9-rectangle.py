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
        number_of_instances (int): total instances of class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        rect = ("".join([str(self.print_symbol)
                         for n in range(self.width)]) + "\n") * self.height
        return rect[:-1]

    def __repr__(self):
        """Returns an officlial string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Detects deletion of a rectangle"""
        Rectangle.number_of_instances -= 1
        print(f'Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with width == height == size"""
        return cls(size, size)
