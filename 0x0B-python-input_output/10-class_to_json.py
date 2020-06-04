#!/usr/bin/python3
""" class to json mod """


def class_to_json(obj):
    """
    Returns the dictionary description of Json serialization obj
    """
    return obj.__dict__
