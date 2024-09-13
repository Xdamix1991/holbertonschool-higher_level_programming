#!/usr/bin/python3
"""
his module provides a function
that prints a text with 2 new lines
after each of these characters: ., ? and :
 """


def text_indentation(text):
    """
     prints a text with 2 new lines
    after each of these characters: ., ? and :
       """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    lenght = len(text)
    while i < lenght:
        print(text[i], end='')
        if text[i] in '.?:':
            print()
            print()
            while i + 1 < lenght and text[i + 1] == ' ':
                i += 1
        i += 1
