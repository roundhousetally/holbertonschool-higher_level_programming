#!/usr/bin/python3
""" square mod bby """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns the size based on width """
        return self.width

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @size.setter
    def size(self, size):
        """ sets the width var of rect class """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be >= 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates args to attrs """
        i = 0
        arglist = ["id", "size", "x", "y"]
        try:
            if args:
                for arg in args:
                    setattr(self, arglist[i], arg)
                    i += 1
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        except IndexError:
            pass
