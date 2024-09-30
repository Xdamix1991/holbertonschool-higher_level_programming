#!/usr/bin/python3
"""
in this module a class that define a student with its attributes
 """


class Student:
    """
    class student
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        else:
            return self.__dict__
