#!/usr/bin/python3
"""Define square class"""


class Square:
    """Representing a square"""

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size (int): the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """used for getting a size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set current size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""

        return (self.__size**2)
