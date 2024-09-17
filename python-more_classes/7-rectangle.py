#!/usr/bin/python3
"""
in this module we create a class called rectangular
 """


class Rectangle:
    """
    This class defines an rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return perimeter

    def __str__(self):
        rectangle_print = ""

        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            rectangle_print += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rectangle_print += "\n"
        return rectangle_print

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1