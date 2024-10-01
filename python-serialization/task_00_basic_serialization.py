#!/usr/bin/python3
"""
in this module 2 function to serialize and deserialize Data
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    data:
        the data to serialize
    filename:
        the json file to write in
    """
    json_data = json.dumps(data)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_data)
        return filename


def load_and_deserialize(filename):
    """
    filename:
        the json file to load from to create Data
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data
