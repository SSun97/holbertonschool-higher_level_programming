#!/usr/bin/python3
""" a module returns the dictionary description with simple data
     structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """a module"""

    return obj.__dict__
