#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Representing rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle

        Args:
            width (int): the width of new rectangle
            height (int): the height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
