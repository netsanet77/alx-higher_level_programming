#!/usr/bin/python3
"""Inherits from function"""


def inherits_from(obj, a_class):
    """
    If the object is an instance of a class that inherited (directly or
    indirectly) from the specified class, return True other wise return False
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
