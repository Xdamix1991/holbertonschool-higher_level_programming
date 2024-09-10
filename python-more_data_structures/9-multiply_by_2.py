#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionaty = {}
    for key, value in a_dictionary.items():
        new_dictionaty[key] = value * 2
    return (new_dictionaty)
