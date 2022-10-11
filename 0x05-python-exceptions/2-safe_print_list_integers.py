#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printedint = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
            printedint += 1
        except (TypeError, ValueError):
            i = i + 1
    print()
    return (printedint)
