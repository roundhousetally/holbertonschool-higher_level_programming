#!/usr/bin/python3
""" replaces element in list without modifying original list """


def new_in_list(my_list, idx, element):
    t = idx
    lt = len(my_list)
    b_list = my_list[:]
    if (my_list):
        for i in range(lt):
            if idx < 0:
                return (b_list)
            if t > (lt - 1):
                return (b_list)
            if i == t:
                b_list[i] = element
                return (b_list)
