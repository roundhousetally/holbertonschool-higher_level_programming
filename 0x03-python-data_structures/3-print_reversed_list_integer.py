#!/usr/bin/python3
""" prints a reversed list of integers """


def print_reversed_list_integer(my_list=[]):
    if (my_list):
        for i in reversed(my_list):
            print("{:d}".format(i))
