#!/usr/bin/python3
def uppercase(str):
    converted = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            converted += chr(ord(i) - 32)
        else:
            converted += i
    print("{}".format(converted))
