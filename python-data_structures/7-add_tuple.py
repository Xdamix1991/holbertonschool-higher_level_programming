#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    result = []
    lenght = min(len(tuple_a), len(tuple_b))

    for i in range(lenght):
        result.append(tuple_a[i] + tuple_b[i])

    return (tuple(result))
