#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4
	module_attributes = dir(hidden_4)
	for attribute in module_attributes:
		if not attribute.startswith("__"):
			print("{:s}".format(attribute))

