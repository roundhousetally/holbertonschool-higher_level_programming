#!/usr/bin/python3
""" Matrix Division Mod """


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    Args: div - what to divide element by """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        for num in row:
            if type(num) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
