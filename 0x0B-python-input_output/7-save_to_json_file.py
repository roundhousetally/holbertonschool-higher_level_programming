#!/usr/bin/python3
""" save to json mod """


def save_to_json_file(my_obj, filename):
    """ writes an obj to a txt file """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
