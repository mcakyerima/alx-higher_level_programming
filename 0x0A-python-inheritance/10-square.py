#!/usr/bin/python3
"""
Module 10-square

Contains subclass Square that inherits from Rectangle
with instantiation of a private attribute size, validated by parent
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
