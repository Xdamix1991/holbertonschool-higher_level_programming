#!/usr/bin/python3
"""
this mosule contains a class named BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        function to check area exeption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks type errors and value errors
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
