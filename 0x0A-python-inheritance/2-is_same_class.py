#!/usr/bin/python3
"""Class that specifies the class of the object"""


def is_same_class(obj, a_class):
    """
    return True if the object is exactly an instance of the
    specified class otherwise return False
    """
    if type(obj) == a_class:
        return True
    return False
