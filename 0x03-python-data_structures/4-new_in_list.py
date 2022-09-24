#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    length = len(my_list)
    for i in range(0, length):
        if idx == i:
            new_list[i] = element
    return new_list
