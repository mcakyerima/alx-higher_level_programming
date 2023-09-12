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
		self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.
        Overrides the str method to return the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
