#!/usr/bin/python3
""" prints a dict by ordered keys """


def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda x: x):
        print("{}: {}".format(key, value))
