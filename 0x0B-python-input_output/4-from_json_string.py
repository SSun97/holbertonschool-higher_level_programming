#!/usr/bin/python3
""" a module decode the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """a function using JSON"""

    return json.loads(my_obj)
