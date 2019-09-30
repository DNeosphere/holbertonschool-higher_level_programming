#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list:
        try:
            print("{}".format(i), end='')
        except:
            pass
        if x == i:
            break
    print()
    return i
