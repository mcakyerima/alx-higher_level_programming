#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def calculate_sum(arguments):
        total = 0
        for i in range(len(arguments)):
            total += int(arguments[i])
        return total

    args = sys.argv[1:]
    if args:
        total_sum = calculate_sum(args)
        print("{:d}".format(total_sum))
