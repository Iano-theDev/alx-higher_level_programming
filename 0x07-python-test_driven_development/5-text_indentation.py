#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these
       characters: . or ? and :
    """
    chars  = ['.', '?', ':']
    end = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in chars:
            print(char + '\n')
            end = True
        elif end and char == ' ':
            continue;
        else:
            end = False
            print(char, end="")
