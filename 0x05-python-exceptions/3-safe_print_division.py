#!/usr/bin/python3
def safe_print_division(a, b):
    division = None
    try:
        division = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(quot))
        return division
