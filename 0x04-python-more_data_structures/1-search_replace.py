#!/usr/bin/python3
"""  replaces all occurrences of an element by another in a new list """


def search_replace(my_list, search, replace):
    new = [] * (len(my_list))
    for item in my_list:
        if item == search:
            new.append(replace)
        else:
            new.append(item)
    return (new)
