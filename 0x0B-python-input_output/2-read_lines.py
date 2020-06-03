#!/usr/bin/python3
""" returns number of lines in a text file """


def read_lines(filename="", nb_lines=0):
    """ counts number of lines in file """
    lineamount = 0
    with open(filename, 'r') as f:
        for line in f:
            if lineamount < nb_lines or nb_lines <= 0:
                print(line, end='')
                lineamount += 1
