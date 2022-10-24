#!/usr/bin/python3
"""Define MyInt class"""


class MyInt(int):
    """class MyInt inherits from int"""
    def __init__(self, myInt):
        """Intializing the value myInt"""
        self.myInt = myInt

    def __eq__(self, other):
        if self.myInt == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.myInt != other:
            return False
        else:
            return True
