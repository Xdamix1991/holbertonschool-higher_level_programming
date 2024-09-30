#!/usr/bin/python3
"""
this module contains a function that dictionary description
 """


def class_to_json(obj):
    """
    obj:
        instance of a class
      """

    return obj.__dict__
