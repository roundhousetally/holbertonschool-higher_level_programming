#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lt = len(my_list)
    for i in range(lt):
        if idx < 0:
            return (my_list)
        if idx > (lt - 1):
            return (my_list)
        if i == idx:
            del (my_list[i])
            return (my_list)
