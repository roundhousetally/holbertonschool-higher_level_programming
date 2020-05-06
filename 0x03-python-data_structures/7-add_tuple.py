#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tublen = len(tuple_a)
    tublen2 = len(tuple_b)
    if tublen > 2 or tublen2 > 2:
        tublen = 2
        tublen2 = 2
    for i in range(tublen):
        tuple_c = tuple(map(sum, zip(tuple_a, tuple_b)))
        return (tuple_c)

#    tuple_c = tuple(map(sum, zip(tuple_a[1:3], tuple_b[1:3])))
#   return (tuple_c)
