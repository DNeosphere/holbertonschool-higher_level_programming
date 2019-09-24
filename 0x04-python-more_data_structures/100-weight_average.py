#!/usr/bin/python3
def weight_average(my_list=[]):

    if my_list == [] or my_list is None:
        return 0

    dividendo = 0
    divisor = 0
    for list_idx in my_list:
        dividendo += list_idx[0] * list_idx[1]
        divisor += list_idx[1]

    return dividendo/divisor
