#!/usr/bin/python3

"""
Module MyList extends from the built in list that 
contains a method print_sorted() that returns the sorted list in an ascending order
"""

class MyList(list):
	""" inherits from the list class

	methods:
	print_sorted(self)
	"""

	def print_sorted(self):
		""" print the sorted list integers in an ascending order"""
		print(sorted(self))
