#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a = key
    b = value
    nd = {a: b}
    if key in a_dictionary:
        a_dictionary[key] = value
        return (a_dictionary)
    else:
        a_dictionary.update(nd)
        return (a_dictionary)
