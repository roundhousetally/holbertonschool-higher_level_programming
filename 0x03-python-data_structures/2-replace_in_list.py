#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    t = idx
    for i in range(len(my_list)):
        if t > (len(my_list)):
            return (my_list)
        if i == t:
            my_list[i] = element
            return (my_list)
