#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary:
        for value in a_dictionary:
            del a_dictionary[value]
            return (a_dictionary)
    else:
        return (a_dictionary)
