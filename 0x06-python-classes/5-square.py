#!/usr/bin/python3
""" Class Square """


class Square:
    """ square """
    def __init__(self, size=0):
        """ private attribute
        Args:
             size - size of square
        """
        self.__size = size

    def area(self):
        """ area """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size var of square class """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints a square """
        if self.size == 0:
            print()
        for i in range(self.size):
            for i in range(self.size):
                print("#", end='')
            print()
