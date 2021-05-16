#!/usr/bin/python3
"""almost a circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)
