#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    t = idx
    lt = len(my_list)
    for i in range(lt):
        if t < 0:
            return (my_list)
        if t > lt:
            return (my_list)
        if i == t:
            my_list[i] = element
            return (my_list)
