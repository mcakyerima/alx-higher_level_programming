#!/usr/bin/python3
"""
Module 8-rectangle

Contains parent class BaseGeometry
with public instance method area and integer_validator

Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry and represents a rectangle.

    :param width: The width of the rectangle.
    :param height: The height of the rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
