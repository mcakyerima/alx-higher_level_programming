#!/usr/bin/python3
""" constains a function that checks if an instance
	belongs to a particular class
"""

def is_same_class(obj, a_class):
	"""
	checks if an instance belongs to a class

	Args:
		obj: the instance to check.
		a_class: the class to check against.

	Returns:
		True of the instance belongs to the class, False otherwise.
	"""

	return isinstance(obj, a_class)

