#!/usr/bin/python3
"""apeend to file module"""


def append_write(filename="", text=""):
    """appends text to a file and returns the number of
    the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
