#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ''
    it2 = 0
    for i in str:
        if it2 != n:
            str_copy += i
        it2 += 1
    return str_copy
