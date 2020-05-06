#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    t = idx
    lt = len(my_list)
    for i in range(lt):
        if idx < 0:
            return (my_list)
        if t > (lt - 1):
            return (my_list)
        if i == t:
            del (my_list[i])
            return (my_list)
