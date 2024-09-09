#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not any(matrix):
        return
    for i in matrix:
        if not i:
            continue
        for j in i:
            if j == i[0]:
                print("{:d}".format(j), end='')
            else:
                print(" {:d}".format(j), end='')
        print()
