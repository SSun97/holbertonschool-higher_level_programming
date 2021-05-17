#!/usr/bin/python3
"""almost a circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of instances"""

        l = [self.id, self.size, self.x, self.y]
        l1 = ['id', 'size', 'x', 'y']

        if len(args) >= 1:
            for i in range(len(args)):
                l[i] = args[i]
            self.__init__(l[1], l[2], l[3], l[0])
        else:
            for k, v in kwargs.items():
                for i in range(len(l1)):
                    if k == l1[i]:
                        setattr(self, l1[i], v)

    def to_dictionary(self):
        """function to display the attributes dictionary"""

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
