#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and print it to stdout"""
    with open(filename) as f:
        r = f.read()
        print(r, end="")
    f.close
