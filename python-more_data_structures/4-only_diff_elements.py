#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    list_1 = list(set_1)
    list_2 = list(set_2)
    unique = set(list_1) ^ set(list_2)
    result = list(unique)
    return (result)
