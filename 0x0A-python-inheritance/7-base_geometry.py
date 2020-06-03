#!/usr/bin/python3
""" geo mod """


class BaseGeometry:
    """ Geo class """
    def area(self):
        """ not imp yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
