#!/usr/bin/python3
""" function that adds two tuples """


def add_tuple(tuple_a=(), tuple_b=()):
    tuplena = len(tuple_a)
    tuplenb = len(tuple_b)
    tuple_c = (0, 0)
    if tuplena < 1:
        tuple_a = tuple_c
    elif tuplena < 2:
        tuple_a = tuple_a[0], 0
    else:
        tuple_a = tuple_a[0], tuple_a[1]
    if tuplenb < 1:
        tuple_b = tuple_c
    elif tuplenb < 2:
        tuple_b = tuple_b[0], 0
    else:
        tuple_b = tuple_b[0], tuple_b[1]
    tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (tuple_c)
