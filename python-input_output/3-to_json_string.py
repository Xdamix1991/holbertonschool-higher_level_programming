#!/usr/bin/python3
"""
this module containe a function tha convert to json format
"""
import json


def to_json_string(my_obj):
    """
    my_obj:
        the object to convert
    return:
        a dat in json format
    """

    objet_json = json.dumps(my_obj)
    return objet_json
