#!/usr/bin/python3
"""A module that writes an Object to a text file,
    using a JSON representation"
"""


import json


def save_to_json_file(my_obj, filename):
    """ A function use json """

    with open(filename, 'w', encoding='utf-8') as f:
        string = json.dumps(my_obj)
        f.write(string)
