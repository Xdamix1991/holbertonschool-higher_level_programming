#!/usr/bin/python3
"""
in this module a function to open a file
"""


def read_file(filename=""):
    """
    dunction to read a file
    filename is the file name to open
    """

    with open(filename) as f:
        for line in f:
            print(line, end="")
