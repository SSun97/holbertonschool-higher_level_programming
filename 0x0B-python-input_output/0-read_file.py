#!/usr/bin/python3
"""A module to read a file"""


def read_file(filename=""):
    """ a function to read a file"""

    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        print(f.read())
