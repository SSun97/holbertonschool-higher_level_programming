#!/usr/bin/python3
""" a module returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """a function using JSON"""

    return json.dumps(my_obj)
