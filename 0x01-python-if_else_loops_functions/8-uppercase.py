#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            c = c - 32
            i = chr(c)
        print("{:s}".format(i), end="")
    print("")

