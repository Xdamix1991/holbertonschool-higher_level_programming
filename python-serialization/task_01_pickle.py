#!/usr/bin/python
"""
this module contains a class, serialize with pickle
"""
import pickle


class CustomObject:

    def __init__(self, name="", age=0, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name : {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        if not filename:
            print("filename not found")
            return None
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            raise Exception("file can't be writen")
            return None

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            print("filename not found")
            return None
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise Exception("cant load the file")
            return None
