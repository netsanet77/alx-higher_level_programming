#!/usr/bin/python3
"""Inherits from function"""


def inherits_from(obj, a_class):
    """
    If the object is an instance of a class that inherited (directly or
    indirectly) from the specified class, return True other wise return False
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
