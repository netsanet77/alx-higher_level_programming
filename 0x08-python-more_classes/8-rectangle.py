#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Representing rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle
        Args:
            width (int): the width of new rectangle
            height (int): the height of new rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """return string"""
        rectangle = ""
        w = self.__width
        h = self.__height
        if w == 0 or h == 0:
            return rectangle
        for i in range(0, h):
            for j in range(0, w):
                rectangle += str(self.print_symbol)
            if i != h - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """return string representation of rectangle to be able to
        recreate a new instance"""
        h = str(self.__height)
        w = str(self.__width)
        return "Rectangle(" + w + ", " + h + ")"

    def __del__(self):
        """print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
