#!/usr/bin/python3
"""
    Write an empty class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class as subclass of Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
