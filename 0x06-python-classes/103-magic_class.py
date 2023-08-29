#!/usr/bin/python3

import math

class MagicClass:
    """
    MagicClass Module:
        Contains the definition of the MagicClass class.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (int or float, optional): The radius of the circle. Default is 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
