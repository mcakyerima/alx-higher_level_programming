#!/usr/bin/python3
"""
This module provides a function for adding attributes to objects.
"""

def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr (str): The attribute name.
        value: The value of the attribute.

    Raises:
        TypeError: If the object doesn't allow adding new attributes.
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
