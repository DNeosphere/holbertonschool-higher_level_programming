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

    def update(self, *args, **kwargs):
        """ Update with args and kwargs """
        attrs = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:

            for i in range(len(args)):
                if i >= len(attrs):
                    break
                else:
                    setattr(self, attrs[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        attrs = ["id", "size", "x", "y"]
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(attrs, values))
