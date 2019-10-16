#!/usr/bin/python3
""" Setattr, getattr and hasattr task """


def add_attribute(object, attr_name, value):
    """  adds a new attribute if its possible """
    if "__slots__" in dir(object) or hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
