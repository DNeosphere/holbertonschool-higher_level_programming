#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ''
    for i in str:
        if i != n:
            str_copy += i
    return str_copy
