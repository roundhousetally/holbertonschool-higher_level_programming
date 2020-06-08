#!/usr/bin/python3
""" base module """


class Base:
    """ base module """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns Json rep of list of dicts """
        if list_dictionaries is None:
            return "[]"
        else:
            import json
            return (json.dumps(list_dictionaries))
