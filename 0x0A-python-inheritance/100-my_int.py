#!/usr/bin/python3
"""
    Write an empty class BaseGeometry
"""


class MyInt(int):
    """a class as subclass of int"""

    def __eq__(self, other):
        if int(self) == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        if int(self) != int(other):
            return False
        else:
            return True
