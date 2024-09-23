#!/usr/bin/python3
"""
this mosule contains a class named BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that heritate from Basegeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        printing = str("[Rectangle] {}/{}".format(self.__width, self.__height))
        return printing


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return super().area()
