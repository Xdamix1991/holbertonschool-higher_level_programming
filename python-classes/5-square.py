#!/usr/bin/python3
"""
This module contains classe of a square
 """


class Square:
    """
     This class represents a square
     size: is a private instance attribut
       """
    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the area of the square
           """
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
