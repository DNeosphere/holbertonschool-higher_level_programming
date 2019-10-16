#!/usr/bin/python3
""" import json module """
import json


def from_json_string(my_str):
    """ takes a json string and get it to python dictionary """
    return json.loads(my_str)
