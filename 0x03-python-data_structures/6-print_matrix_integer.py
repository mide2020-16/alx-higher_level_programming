#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i, j = 0, 0
    for row in matrix:
        for num in row:
            print("{}".format(num), end=" ")
        print()

