#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lenli = len(my_list)
    res = [0] * lenli
    if (my_list):
        for i in my_list:
            if my_list[i] % 2 == 0:
                res[i] = True
            else:
                res[i] = False
        return (res)
