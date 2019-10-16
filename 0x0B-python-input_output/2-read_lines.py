#!/usr/bin/python3
""" REad n lines """


def read_lines(filename="", nb_lines=0):
    """ read n lines, or the whole text """
    count = 0
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end='')
        else:
            for a_line in range(nb_lines):
                print(a_file.readline(), end='')
