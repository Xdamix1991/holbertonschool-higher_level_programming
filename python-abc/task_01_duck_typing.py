#!/usr/bin/python3
import math
"""
this module contains classes to creat shapes
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    abstract parrrent class of shapes
    """

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = (self.radius ** 2) * math.pi
        return result

    def perimeter(self):
        return math.pi * self.radius * 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = self.height * self.width
        return result

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(arg):
    ar = arg.area()
    per = arg.perimeter()
    print("ar is {}".format(ar))
    print("per is {}".format(per))
