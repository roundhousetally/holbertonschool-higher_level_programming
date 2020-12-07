#!/usr/bin/python3
""" finds the biggest integer of a list """


def max_integer(my_list=[]):
    if (my_list):
        maxx = sorted(my_list)[-1]
        return (maxx)
