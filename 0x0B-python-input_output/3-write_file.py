#!/usr/bin/python3
""" writes  a string to txt file and returns number of chars written """


def write_file(filename="", text=""):
    """ ditto """
    chars = len(text)
    with open(filename, 'w') as f:
        f.write(text)
        return (chars)
