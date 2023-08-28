#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if isinstance(item, int):
                print("{:d}".format(item), end=" ")
                count += 1
                if count >= x:
                    break

        print()
        return count
    except IndexError:
        return count
