#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for first, second in sorted(a_dictionary.items()):
        print(f"{first} : {second}")
