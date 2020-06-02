#!/usr/bin/python3
""" exact same obj mod """


def is_same_class(obj, a_class):
    """ checks if obj is exactly an instance of spec class """
    if type(obj) == a_class:
        return True
    else:
        return False
