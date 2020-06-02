#!/usr/bin/python3
""" mod """


def inherits_from(obj, a_class):
    """
    checks if obj is instance of a class that inherited from the
    specified class
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
