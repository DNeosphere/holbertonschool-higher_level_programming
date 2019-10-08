#!/usr/bin/python3
"""
Definition of a rectangle class
"""


class Rectangle:
    """ Rectangle definition """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization of the instances
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Destructor MUAHAHA """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """ returns a graphical demonstration of the desired rectangle """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """ returns traditional formal string """
        repr_str = self.__class__.__name__
        return "{}({}, {})".format(repr_str, self.__width, self.__height)

    @property
    def width(self):
        """ Width of the triangle """
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
        """ Height of the rectangle """
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

        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
