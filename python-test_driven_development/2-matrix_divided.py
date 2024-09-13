#!/usr/bin/python3
"""
This module provides a function that devides two integers of a matrix.
"""


def matrix_divided(matrix, div):
    """
     Divides all elements of a matrix by a given number

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        A new matrix with divided values rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")

    len_of_row = len(matrix[0])
    if not all(len(row) == len_of_row for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for number in row:
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = []
        for row in matrix:
            new_row_divided = [round(i / div, 2) for i in row]
            new_matrix.append(new_row_divided)
    return new_matrix
