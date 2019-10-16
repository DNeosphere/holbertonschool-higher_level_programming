#!/usr/bin/python3
""" DEfinition of a class """


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self_dict = self.__dict__
        if type(attrs) == list:
            n_dict = {}
            for item in self_dict.keys():
                if item in attrs:
                    n_dict[item] = self_dict[item]
            return n_dict
        else:
            return self_dict
