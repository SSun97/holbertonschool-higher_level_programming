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
        """Doc"""

        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
