#!/usr/bin/python3

"""
Module 7-base_geometry
This module defines the BaseGeometry class. with public instance area and integer_validation
"""

class BaseGeometry:
    """
    The BaseGeometry class is a base class for geometry-related classes.
	Methods:
		area(slef)
		integer_validator(self, name, value)
    """

	def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
        """
        Validates the value as an integer and checks if it's greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
		if type(value) is not int:
			raise TypeError(f"{:s} must be an integer".format(name))
		if value <= 0:
			raise ValueError(f"{:s} must be greater than 0".format(name))
