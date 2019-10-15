#!/usr/bin/python3
""" usage of type """


def is_same_class(obj, a_class):
    """ check wheter an object is the SAME type of another """
    if type(obj) is a_class:
        return True
    else:
        return False
