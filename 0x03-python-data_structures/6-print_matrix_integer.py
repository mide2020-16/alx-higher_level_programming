#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for num in row:
            i = i + 1
            print("{:d}".format(num), end=" " if i < 3 else "")
        i = 0
        print()

