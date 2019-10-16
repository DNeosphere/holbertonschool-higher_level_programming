#!/usr/bin/python3
""" import json module """
import json


def load_from_json_file(filename):
    """ open a json file, read it an convert it to a python object """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
