#!/usr/bin/python3
"""
This module contains classe of a square
 """


class Square:
    """
     This class represents a square
     type: is a public class attribute
       """
    def __init__(self, size=0):
        """
        function to initialize a square size
           """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
