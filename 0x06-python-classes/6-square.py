#!/usr/bin/python3
""" Class Square """


class Square:
    """ square """
    def __init__(self, size=0, position=(0, 0)):
        """ private attribute
        Args:
             size - size of square
             position - coordinates of a square        """
        self.size = size
        self.position = position

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
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)

    @property
    def position(self):
        """ retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the coord position of square """
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif len(value) > 2 or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
