#!/usr/bin/python3
"""
in this mosule a function writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    my_obj:
        object to convert
    filename:
        to put the object into
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
