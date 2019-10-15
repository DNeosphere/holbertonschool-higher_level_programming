#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
