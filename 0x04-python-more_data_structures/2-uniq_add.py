#!/usr/bin/python3
""" function that adds all unique integers in a list """


def uniq_add(my_list=[]):
    my_set = set(my_list)
    sumset = sum(my_set)
    return (sumset)
