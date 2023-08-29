#!/usr/bin/python3

"""
Square Module:
    Contains the definition of the Square class.
"""


class Square:
    """
    Square class:
        Defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
