#!/usr/bin/python3
""" finds element at index """


def element_at(my_list, idx):
    i = idx + 1
    if (my_list == '\0'):
        return (None)
    if idx < 0:
        return (None)
    if (i > (len(my_list))):
        return (None)
    else:
        return (my_list[(i - 1)])
