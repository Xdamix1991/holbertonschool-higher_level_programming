#!/usr/bin/python3
"""
in this module function that generate pascal triangle
 """


def pascal_triangle(n):
    """
    n the size of the triangle
    """

    liste = []

    for i in range(n):
        liste.append([1] * (i + 1))

        for j in range(1, i):
            liste[i][j] = liste[i - 1][j - 1] + liste[i - 1][j]
    return liste
