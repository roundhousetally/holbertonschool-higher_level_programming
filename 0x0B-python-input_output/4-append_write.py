#!/usr/bin/python3
""" writes  a string to txt file and returns number of chars written """


def append_write(filename="", text=""):
    """ ditto """
    chars = len(text)
    with open(filename, 'a+') as f:
        f.write(text)
        return (chars)
