#!/usr/bin/python3
"""
in this module you ll find a class CountedIterator
"""


class CountedIterator:

    def __init__(self, obj):
        self.obj = obj
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.obj):
            result = self.obj[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration("no more items")

    def get_count(self):
        return self.counter


def tests():
    list1 = [1, 2, 5, 6, 8]
    iterator = CountedIterator(list1)
    for item in iterator:
        pass
    number_of_items = iterator.get_count()
    print(number_of_items)
    return number_of_items


if __name__ == "__main__":
    tests()
