#!/usr/bin/python3
"""
in this module a class named animal is created
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    abstract class Animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    substract class from Animal
    """

    def sound(self):
        self.__sound = "Bark"
        return self.__sound


class Cat(Animal):
    """
    substract class from Animal
    """

    def sound(self):
        self.__sound = "Meow"
        return self.__sound
