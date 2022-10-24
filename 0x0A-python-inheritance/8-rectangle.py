#!/usr/bin/python3
"""A class of BaseGeomety"""


class BaseGeometry:
    """A class with public instance methods"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializing new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
