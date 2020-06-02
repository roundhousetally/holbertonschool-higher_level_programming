#!/usr/bin/python3
""" mod """


def is_kind_of_class(obj, a_class):
    """ checks if obj is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
