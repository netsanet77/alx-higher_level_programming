#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    try:
        for i, j in zip(my_list_1, my_list_2):
            new_list = i / j
        return (str(new_list))
    except ValueError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")

