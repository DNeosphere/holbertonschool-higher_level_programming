#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_list = (sorted(a_dictionary))
    for key in a_list:
        print("{}: {}".format(key, a_dictionary[key]))
