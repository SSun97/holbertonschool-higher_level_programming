#!/usr/bin/python3
"""A empty class Square that defines a square

This module provides a simple version of class

"""


class Square:
    """The class definition"""

    def __init__(self, size):
        """init"""
        self.size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, v):
        """set the size"""
        if type(v) is not int:
            raise TypeError("size must be an integer")
        elif v < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = v

    def area(self):
        """calculate the area"""
        return self.__size ** 2
