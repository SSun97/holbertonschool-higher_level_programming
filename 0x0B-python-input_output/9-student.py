#!/usr/bin/python3
"""a class of students"""


class Student:
    """a class of students"""

    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
