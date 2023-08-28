#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
	for i in mylist[:x]:
	    print("{}".format(i))
	    count += 1

	print()
	return count
    except IndexError:
        print()
	return count
