#!/usr/bin/python3
""" reads utf and prints to standard out """


def read_file(filename=""):
    """ reads a file and prints to stdout """
    with open(filename, 'r') as f:
        fileinfo = f.read()
        print(fileinfo, end='')
