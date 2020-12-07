#!/usr/bin/python3
""" removes all characters C and c from a string """


def no_c(my_string):
    mistring = ""
    for i in my_string:
        if (i != 'c' and i != 'C'):
            mistring = mistring + i
    return (mistring)
