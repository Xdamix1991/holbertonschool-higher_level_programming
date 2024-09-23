#!/usr/bin/python3
"""
This module contains a mylist class
 """


class MyList(list):
    """
     this class defines
    """

    def print_sorted(self):
        if not isinstance(self, list):
            raise TypeError("must be a list")
        for i in self:
            if not isinstance(i, int):
                raise TypeError("must be an integer")
        print(sorted(self))
