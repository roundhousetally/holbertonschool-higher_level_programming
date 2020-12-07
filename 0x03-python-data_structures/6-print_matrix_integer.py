#!/usr/bin/python3
""" function that prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    if (matrix[0]):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if c < (len(matrix[r]) - 1):
                    print("{:d}".format(matrix[r][c]), end=' ')
                else:
                    print("{:d}".format(matrix[r][c]), end='')
            print()
    else:
        print()
