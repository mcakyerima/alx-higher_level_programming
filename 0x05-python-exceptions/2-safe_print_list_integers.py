#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if count < x and isinstance(i, int):
                print("{:d}".format(i), end=" ")
                count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
