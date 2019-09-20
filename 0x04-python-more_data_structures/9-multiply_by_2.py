#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = a_dictionary.copy()
    for value in n_dictionary:
        n_dictionary[value] *= 2
    return n_dictionary
