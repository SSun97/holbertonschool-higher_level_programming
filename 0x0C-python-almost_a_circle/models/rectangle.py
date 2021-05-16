#!/usr/bin/python3
"""almost a circle"""
from models.base import Base


class Rectangle(Base):
    """a class of rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """calculate area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """disolay a rectangle"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """print function"""

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)
    def update(self, *args):
        """update attributes of instances"""

        l = [self.id, self.__width, self.__height,
                    self.__x, self.__y]
        l1 = ['id', 'width', 'height', 'x', 'y']

        if len(args) >= 1:
            for i in range(len(args)):
                l[i] = args[i]
            self.__init__(l[1], l[2], l[3], l[4], l[0])
        else:
            for k, v in kwargs.items():
                for i in range(len(l1)):
                    if k == l1[i]:
                        setattr(self, l1[i], v)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
