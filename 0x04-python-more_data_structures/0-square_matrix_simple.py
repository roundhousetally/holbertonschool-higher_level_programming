#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [] * (len(matrix))

    new = [[elem*elem for elem in inner] for inner in matrix]
    return (new)
