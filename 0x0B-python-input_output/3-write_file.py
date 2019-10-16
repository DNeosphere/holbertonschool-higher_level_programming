#!/usr/bin/python3
""" Write into a file """


def write_file(filename="", text=""):
    """ write a file """
    chars_w = 0
    with open(filename, mode='w', encoding='utf-8') as a_file:
        chars_w = a_file.write(text)
        return chars_w
