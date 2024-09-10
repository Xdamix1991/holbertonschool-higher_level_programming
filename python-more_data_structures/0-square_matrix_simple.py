#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix or not any(matrix):
        return (None)
    result = []
    for i in matrix:
        result.append([j ** 2 for j in i])
    return (result)
