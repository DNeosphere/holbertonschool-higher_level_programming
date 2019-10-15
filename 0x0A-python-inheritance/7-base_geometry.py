#!/usr/bin/python3
""" Example of a class """


class BaseGeometry:
    def area(self):
        """ Raise exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Integer validation """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{}  must be greater than 0".format(name))
