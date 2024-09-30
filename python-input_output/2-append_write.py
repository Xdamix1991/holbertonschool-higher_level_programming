#!/usr/bin/python3
"""
in this module a function to write in a file
"""


def append_write(filename="", text=""):
    """
    filename:
        the file to open or to creat
    text:
        the text to write
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
