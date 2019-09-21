#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None

    dividendo = 0
    divisor = 0
    for list_idx in my_list:
        dividendo += list_idx[0] * list_idx[1]
        divisor += list_idx[1]

    return dividendo/divisor
