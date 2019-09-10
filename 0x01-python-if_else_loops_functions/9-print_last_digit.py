#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    number = number % 10
    print("{}".format(number), end='')
    return number
