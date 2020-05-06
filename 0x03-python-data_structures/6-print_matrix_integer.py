#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if c < (len(matrix) - 1):
                    print("{:d}".format(matrix[r][c]), end=' ')
                else:
                    print("{:d}".format(matrix[r][c]), end='')
            print("")
    else:
        return
