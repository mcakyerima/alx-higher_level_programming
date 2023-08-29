#!/usr/bin/python3

"""
Square Module:
    Contains the definition of the Square class.
"""


class Square:
    """
    Square class:
        Defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

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
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position attribute.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters and positioning.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        result = ""
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.strip()

