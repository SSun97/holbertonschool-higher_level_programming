#!/usr/bin/python3
"""
    Write a function that returns True if the object is exactly an\
     instance of the specified class ; otherwise False
"""


def def is_kind_of_class(obj, a_class):
    """Doc """

    if isinstance(obj, a_class):
        return True
    else:
        return False
