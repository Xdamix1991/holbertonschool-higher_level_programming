#!/usr/bin/python3
"""
this module contains a function
"""


def inherits_from(obj, a_class):
    """
    checks if the abject inherited (directly or indirectly) from class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
