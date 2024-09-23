#!/usr/bin/python3
"""
this module contains a function
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the abject came from classe or subb class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
