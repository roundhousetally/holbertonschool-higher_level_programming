#!/usr/bin/python3
""" returns number of lines in a text file """


def number_of_lines(filename=""):
    """ counts number of lines in file """
    lineamount = 0
    with open(filename, 'r') as f:
        for line in f:
            lineamount += 1
        return (lineamount)
