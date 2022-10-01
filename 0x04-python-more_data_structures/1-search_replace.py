#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_liist = my_list.copy()
    for i in range(0, len(my_liist)):
        if my_liist[i] == search:
            my_liist[i] = replace
    return my_liist
