#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = [0] * list_length
    c = 0
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")
        finally:
            n_list[i] = c
    return n_list
