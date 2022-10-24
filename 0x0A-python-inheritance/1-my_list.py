#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """MyList that that define instance method"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(list(self)))
