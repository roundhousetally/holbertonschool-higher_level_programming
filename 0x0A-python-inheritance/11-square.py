#!/usr/bin/python3
""" square mod """
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """ init """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size * self.__size

    def __str__(self):
        """ returns sq rep """
        return "[Square] {}/{}".format(self.__size, self.__size)
