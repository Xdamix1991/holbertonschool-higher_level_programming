#!/usr/bin/python3
"""
in this module
"""


class VerboseList(list):
    """
    pop notifications
    """

    def __init__(self, *args):
        super().__init__(*args)

    def append(self, item):

        super().append(item)
        (print("Added [{}] to the list.".format(item)))

    def extend(self, *item):
        numbre = len(*item)
        super().extend(*item)
        return (print("Extended the list with [{}] items".format(numbre)))

    def remove(self, item):
        print("Removed [{}] from the list".format(item))
        try:
            super().remove(item)
        except ValueError:
            raise ValueError("item not found")

    def pop(self, *args):
        try:
            item = super().pop(*args)
        except ValueError:
            raise ValueError("item not found")
        print("Popped [{}] from the list".format(item))


def tests():
    test = VerboseList()
    test.append(5)
    test.extend([1, 2, 3])
    test.remove(6)
    test.pop(2)
    print(test)


if __name__ == "__main__":
    tests()
