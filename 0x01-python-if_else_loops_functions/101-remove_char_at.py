#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    length = len(str)
    if n < 0:
        print(f"{str}")
    else:
        for i in range(0, length):
            if i != n:
                new_str = new_str + str[i]
        print(f"{new_str}")
