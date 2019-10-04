#!/bin/usr/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')

    n_str = text.replace('?', '?\n\n')
    n_str = n_str.replace('.', '.\n\n')
    n_str = n_str.replace(':', ':\n\n')

    print("\n".join([li.strip() for li in n_str.split("\n")]), end="")
