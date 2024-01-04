#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle
"""

class Rectangle:
    """ class rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
         """ width
        """
        return self.__width

    @width.setter
    def width(self, value):
           """ width setter
        """
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
         """height
        """
        return self.__height

    @height.setter
    def height(self, value):
         """ height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


Rec = Rectangle(0, 0)
