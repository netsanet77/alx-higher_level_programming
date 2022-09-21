#!/usr/bin/python3
def pow(a, b):
    result = 1
    if a == 0:
        return
    if b < 0:
        power = -b
    else:
        power = b
    for i in range(power):
        result = result * a
    if b < 0:
        return 1 / result
    else:
        return result
