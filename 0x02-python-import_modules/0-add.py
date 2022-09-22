#!/usr/bin/python3
if __name__ != '__import__':
    from add_0 import add
    a = 1
    b = 2
    s = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, s))
