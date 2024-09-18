#!/usr/bin/python3
"""
This module contains classe of a square
 """


class Square:
    """
     This class represents a square
     size: is a private instance attribut
       """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
         not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        """
        calculates the area of the square
           """
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for i in range(self.__postion[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__postion[0] + "#" * self.__size)
