#!/usr/bin/python3
""" Write to a file using append """


def append_write(filename="", text=""):
    """ Write using append """
    chars_a = 0
    with open(filename, mode='a', encoding='utf-8') as a_file:
        chars_a = a_file.write(text)
        return chars_a
