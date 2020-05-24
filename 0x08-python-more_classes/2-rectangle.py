#!/usr/bin/python3
""" Full Rectangle """


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ private attribute
        Args:
             width and height of a rect
        """
        self.__width = width
        self.__height = height

    def area(self):
        """ area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return((self.__width * 2) + (self.__height * 2))

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
