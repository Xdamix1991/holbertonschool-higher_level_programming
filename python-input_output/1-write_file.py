#!/usr/bin/python3
"""
in this module a function to write in a file
"""


def write_file(filename="", text=""):
    """
    filename:
        the file to open or to creat
    text:
        the text to write
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text, end="")
