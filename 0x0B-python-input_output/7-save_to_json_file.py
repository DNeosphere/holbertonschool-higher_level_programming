#!/usr/bin/python3
""" Import json module """
import json


def save_to_json_file(my_obj, filename):
    """ save an object to a file in JSON representation """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
