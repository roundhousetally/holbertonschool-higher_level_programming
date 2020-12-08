#!/usr/bin/python3
""" returns a key with the biggest int value """


def best_score(a_dictionary):
    if a_dictionary:
        new_dict = max(a_dictionary, key=a_dictionary.get)
        return (new_dict)
    else:
        return (None)
