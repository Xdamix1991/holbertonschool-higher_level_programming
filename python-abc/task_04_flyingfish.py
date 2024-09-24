#!/usr/bin/python3
"""
in this module you ll find a class named: FlyingFish
"""


class Fish:
    """
    class fish
    """

    def __init__(self):
        self.swim_message = "The fish is swimming"
        self.habitat_message = "The fish lives in water"

    def swim(self):
        print(self.swim_message)

    def habitat(self):
        print(self.habitat_message)


class Bird:
    """
    classe bird
    """

    def __init__(self, fly, habitat):
        self.fly_message = "The bird is flying"
        self.habitat_message = "The bird lives in the sky"

    def fly(self):
        print(self.fly_message)

    def habitat(self):
        print(self.habitat_message)


class FlyingFish(Fish, Bird):
    """
    child class from nird and fish
    """

    def __init__(self):
        super().__init__()

    def fly(self):
        self.fly = "The flying fish is soaring!"
        print(self.fly)

    def swim(self):
        self.swim = "The flying fish is swimming!"
        print(self.swim)

    def habitat(self):
        self.habitat = "The flying fish lives both in water and the sky!"
        print(self.habitat)


def tests():
    test = FlyingFish()
    test.fly()
    test.swim()
    test.habitat()

    print(FlyingFish.mro())
    print(FlyingFish.__mro__)


if __name__ == "__main__":
    print(tests())
