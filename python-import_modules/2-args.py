#!/usr/bin/python3
import sys


def print_argv():
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))

    for count in range(1, len(sys.argv)):
        print("{}: {}".format(count, sys.argv[count]))


if __name__ == "__main__":
    print_argv()
