#!/usr/bin/python3
""" Finds a poeak in an unsorted array """


def find_peak(list_of_integers):
    """ Finds a peak in an unsorted array """

    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return ((list_of_integers[0], list_of_integers[1])
                [list_of_integers[0] < list_of_integers[1]])

    mid = int((len(list_of_integers) - 1) / 2)

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid + 1])
