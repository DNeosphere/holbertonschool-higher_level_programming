#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" Class inheritance """


class Square(Rectangle):
    """ defines a Square """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Finds the area of a square, using inheritance of rectangle """
        return super().area()
