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
    def __init__(self, sound):
        self.__sound = sound

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    substract class from Animal
    """

    def __init__(self):
        super().__init__("Bark")

    def sound(self):
        return self._Animal__sound

    def __str__(self):
        sound_dog = str("{}".format(self.sound))
        return sound_dog


class Cat(Animal):
    """
    substract class from Animal
    """

    def __init__(self):
        super().__init__("Meow")

    def sound(self):
        return self._Animal__sound

    def __str__(self):
        sound_cat = str("{}".format(self.sound))
        return sound_cat
