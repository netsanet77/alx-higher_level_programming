#!/usr/bin/python3
"""Define square class"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
        size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
