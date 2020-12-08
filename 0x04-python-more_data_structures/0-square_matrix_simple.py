#!/usr/bin/python3
""" function that computes the square value of all integers of a matrix """


def square_matrix_simple(matrix=[]):
    new = [] * (len(matrix))

    new = [[elem*elem for elem in inner] for inner in matrix]
    return (new)
