#!/usr/bin/python3
"""
Definition of a rectangle class
"""


class Rectangle:
    """ Rectangle definition """
    def __init__(self, width=0, height=0):
        """
        Initialization of the instances
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ prints a graphical demonstration of the desired rectangle """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += '#' * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        perim = self.__height * self.__width
        return perim

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
