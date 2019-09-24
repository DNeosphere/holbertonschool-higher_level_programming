#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None

    dicc = {ord('c'): None, ord('C'): None}
    my_string_2 = my_string.translate(dicc)
    return my_string_2
