#!/usr/bin/python3
"""file append function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and return number of character
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
