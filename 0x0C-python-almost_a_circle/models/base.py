#!/usr/bin/python3
""" definition of a class Base """
import json
from turtle import *


class Base:
    """ Definition of class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file """

        fname = cls.__name__ + ".json"
        lista = []
        with open(fname, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                a_file.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lista.append(obj.to_dictionary())
                a_file.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set """
        dummy_cls = cls(1, 1)
        dummy_cls.update(**dictionary)
        return dummy_cls

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """

        try:
            instance_l = []
            with open(cls.__name__ + ".json", mode='r') as a_file:
                j_file = cls.from_json_string(a_file.read())
                for dic in j_file:
                    instance_l.append(cls.create(**dic))
                return instance_l
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws using turtle """
        for rec in list_rectangles:
            setpos(rec.x, rec.y)
            width(4)
            pencolor('red')
            forward(rec.width)
            right(90)
            forward(rec.height)
            right(90)
            forward(rec.width)
            right(90)
            forward(rec.height)
            right(90)
            width(0)

        setpos(0, 0)
        for sqr in list_squares:
            pencolor('blue')
            setpos(sqr.x, sqr.y)
            width(7)
            forward(sqr.width)
            right(90)
            forward(sqr.width)
            right(90)
            forward(sqr.width)
            right(90)
            forward(sqr.width)
            right(90)
            width(0)
