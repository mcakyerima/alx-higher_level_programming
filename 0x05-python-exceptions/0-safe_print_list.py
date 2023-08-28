#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print("{}".format(my_list[count]), end="")
            count += 1
        print()
    except:
        print()
    return count
