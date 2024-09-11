#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
      Returns:
        int: The result of adding a and b after casting them to integers.
    Raises: TypeError: If a or b are neither int nor float.
    """

    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")

    result = a + b
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
