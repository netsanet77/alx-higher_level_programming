#!/usr/bin/python3
"""square class inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation"""
    def __init__(self, size):
        """Initializing new square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of square"""
        return self.__size ** 2

    def __str__(self):
        """return string"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
