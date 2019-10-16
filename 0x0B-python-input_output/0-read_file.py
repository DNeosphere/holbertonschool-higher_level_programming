#!/usr/bin/python3
""" read from a file """


def read_file(filename=""):
    """ reads the whooole file """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
