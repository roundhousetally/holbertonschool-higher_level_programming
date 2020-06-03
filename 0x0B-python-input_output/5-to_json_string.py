#!/usr/bin/python3
""" Json mod """


def to_json_string(my_obj):
    """ returns the json rep of an object """
    import json
    return (json.dumps(my_obj))
