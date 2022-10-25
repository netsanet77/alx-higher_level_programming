#!/usr/bin/python3
"""Write to file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters"""

    with open(filename, "w+", encoding="utf-8") as f:
        w = f.write(text)
    return w
