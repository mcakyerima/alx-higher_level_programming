#!/usr/bin/python3
"""
Module 11-square

Contains a subclass Square that inherits from Rectangle
with instantiation of a private attribute size, validated by parent
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle, which inherits from BaseGeometry.
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.
        Args:
            size (int): Private attribute representing the size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
