#!/usr/bin/python3
""" base module """
import json


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
            return (json.dumps(list_dictionaries))

    def from_json_string(json_string):
        """ returns the list from the JSON string rep """
        if json_string is None or len(jsonstring) == 0:
            return "[]"
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json str rep to file """
        fn = cls.__name__ + ".json"
        strlist = []
        with open(fn, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                strlist = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(strlist))
