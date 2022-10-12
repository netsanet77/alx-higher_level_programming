#!/usr/bin/python3
"""Define square class"""


class Square:
    """Representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square
        Args:
            size (int): the size of the new square
            position (int): position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """used for getting a size of square"""
        return self.__size

    @property
    def position(self):
        """Get the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set current size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """return the current square area"""
        return (self.__size**2)

    def my_print(self):
        """print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for k in range(1, self.__position[1] + 1):
            print()
        for i in range(0, self.__size):
            for space in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
