#!/usr/bin/python3
"""
    Write an empty class BaseGeometry
"""


class BaseGeometry:
    """Write an empty class BaseGeometry"""

    def area(self):
        """area function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """a class as subclass of BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
