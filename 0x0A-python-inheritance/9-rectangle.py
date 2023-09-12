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
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        super().__init__()  # Call the constructor of the parent class
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Private attribute for width
        self.__height = height  # Private attribute for height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description for str() method."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
