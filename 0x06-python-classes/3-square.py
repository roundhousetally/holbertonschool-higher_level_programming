#!/usr/bin/python3
""" Class Square """


class Square:
    """ square """
    def __init__(self, size=0):
        """ private attribute
        Args:
             size - size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area """
        return (self.__size * self.__size)
