#!/usr/bin/python3
""" a module to write a string to a text file """


def write_file(filename="", text=""):
    """ a function to write a string to a text file"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
