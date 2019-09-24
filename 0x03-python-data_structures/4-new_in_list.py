#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_2 = my_list
    if idx < 0 or idx >= len(my_list):
        return my_list_2
    my_list_2 = my_list[:]
    my_list_2[idx] = element
    return my_list_2
