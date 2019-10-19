#!/usr/bin/python3
""" Square class, inherits from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width
    @size.setter
    def size(self, size):
        """ seize setter """
        self.width = size
        self.height = size

    def __str__(self):
        """ overloading str method """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))
