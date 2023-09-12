#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare against.
    :return: True if obj is an instance of a class inherited from a_class, False otherwise.
    """
    # Get the list of base classes for the object's class.
    base_classes = obj.__class__.__bases__

    # Check if a_class is in the base classes or any of their subclasses.
    for base_class in base_classes:
        if base_class is a_class or issubclass(base_class, a_class):
            return True

    return False
