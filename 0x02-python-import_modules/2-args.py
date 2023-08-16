#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    length = len(arguments)
    print("{:d} {:s}{:s}".
          format(length,
                 "arguments" if length != 1 else "argument",
                 "." if length == 0 else ":"))
    for index, value in enumerate(arguments):
        print("{:d}: {:s}".format(index + 1, value))
