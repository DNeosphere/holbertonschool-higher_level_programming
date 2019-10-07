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
        """ returns a graphical demonstration of the desired rectangle """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += '#' * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """ returns traditional formal string """
        repr_str = self.__class__.__name__
        return "{}({}, {})".format(repr_str, self.__width, self.__height)

    @property
    def width(width):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

    @property
    def height(height):
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
        if self.__height == 0 or self.__width == 0:
            return 0

        perim = self.__height * self.__width
        return perim

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)
