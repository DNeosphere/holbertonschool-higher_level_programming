#!/usr/bin/python3
"""
adds two integers
>>> add_integer(1,3)
4
"""
def add_integer(a, b=98):
    """
    Function that adds two integers
    """

    if a is None:
        raise TypeError('a must be an integer')

    elif b is None:
        raise TypeError('b must be an integer')

    elif not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    else:
        return int(a) + int(b)
