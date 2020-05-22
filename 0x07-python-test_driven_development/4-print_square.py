#!/usr/bin/python3
""" Mod that prints a very exciting square made of hashes """


def print_square(size):
    """ func prints a square of hashes """
    if type(size) is float and size < 0 or type(size) is not int:
        raise TypeError("size must be an integer")
    if size is 0:
        print()
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end='')
            print()
