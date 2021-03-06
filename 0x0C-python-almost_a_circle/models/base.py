#!/usr/bin/python3
"""almost a circle"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """decode the json string to a list of dictionaries"""

        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to save a file"""

        if list_objs is None:
            list_objs = []
        json_string_list = []
        for obj in list_objs:
            json_string_list.append(obj.to_dictionary())
        json_string = cls.to_json_string(json_string_list)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creat a dummy instance"""

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        if cls.__name__ == 'Square':
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method for load from file"""

        file_path = cls.__name__ + ".json"
        if not os.path.exists(file_path):
            return []
        else:
            with open(file_path, 'r') as f:
                list = cls.from_json_string(f.read())
        list_rect = []
        for rect in list:
            list_rect.append(cls.create(**rect))
        return list_rect
