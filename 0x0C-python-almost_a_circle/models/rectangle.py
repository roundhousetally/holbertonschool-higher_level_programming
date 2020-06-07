#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value of x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets valye of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """ retreive width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width var of rect class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height var of rect class """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rec """
        return (self.__width * self.__height)
