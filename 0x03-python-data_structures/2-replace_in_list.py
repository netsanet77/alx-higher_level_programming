#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    for i in range(0, length):
        if idx == i:
            my_list[i] = element
    return my_list
