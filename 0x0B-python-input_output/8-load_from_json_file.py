#!/usr/bin/python3
""" creates an obj from json file """


def load_from_json_file(filename):
    """ creates an obj from json file """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
