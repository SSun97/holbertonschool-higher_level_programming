#!/usr/bin/python3
"""A module that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """ A function use json """

    with open(filename, 'r', encoding='utf-8') as f:
        string = json.load(f)
        return string
