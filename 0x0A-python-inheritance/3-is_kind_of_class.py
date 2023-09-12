#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains method is_kind_of_class
it returns true if object is instance of class or inherited class, false otherwise
"""

def is_kind_of_class(obj, a_class):
	"""
	checks   if the object is an instance of,or if the
	object is an instance of a class that inherited from, the specified class.

	Args:
		obj: the object to check.
		a_class: the class to check against.

	Returns:
		True if the object belongs to the class or inherited from, False otherwise
	"""

	return isinstance(obj, a_class)

