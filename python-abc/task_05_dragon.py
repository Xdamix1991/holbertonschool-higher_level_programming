#!/usr/bin/python3
"""
in this module we create a mixin class
"""


class SwimMixin:
    """
    swim class
    """

    def __init__(self):
        self.swim_message = "The creature swims!"

    def swim(self):
        print(self.swim_message)


class FlyMixin:
    """
    fly class
    """

    def __init__(self):
        self.fly_message = "The creature flies!"

    def fly(self):
        print(self.fly_message)


class Dragon(SwimMixin, FlyMixin):
    """
    dragon class
    """

    def __init__(self):
        SwimMixin.__init__(self)
        FlyMixin.__init__(self)
        self.roat_message = "The dragon roars!"

    def roar(self):
        print(self.roat_message)

    def swim(self):
        print(self.swim_message)

    def fly(self):
        print(self.fly_message)


def tests():
    test = Dragon()
    test.fly()
    test.roar()
    test.swim()
    print(test)


if __name__ == "__main__":
    tests()
