#!/usr/bin/python3
""" function that returns an obj represented by a JSON string """


def from_json_string(my_str):
    """ returns an obj """
    import json
    return (json.loads(my_str))
