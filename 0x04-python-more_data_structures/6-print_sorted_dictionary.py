#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda x: x):
        print("{}: {}".format(key, value))