#!/usr/bin/python3
""" prints a list of integers """


def print_list_integer(my_list=[]):
    i = 0
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
