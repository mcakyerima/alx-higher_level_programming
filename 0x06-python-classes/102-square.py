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

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size attribute.

        Args:
            value (int or float): The new size value.

        Raises:
            TypeError: If the value is not a number (integer or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparison based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of this square is less or equal, False otherwise.
        """
        return self.area() <= other.area()

