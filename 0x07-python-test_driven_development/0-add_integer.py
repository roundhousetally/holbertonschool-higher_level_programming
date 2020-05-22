#!/usr/bin/python3
""" Add Integer Mod """


def add_integer(a, b=98):
    """ Returns the sum of 2 integers or floats """
    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
