#!/usr/bin/python3
"""almost a circle"""
import json


class Base:

    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """encode the dictionaries to json string"""

        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
