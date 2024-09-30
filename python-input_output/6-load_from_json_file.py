#!/usr/bin/python3
"""
this module contains a function that creats
an object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    filename the file to creat
    """

    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f)
        return obj
