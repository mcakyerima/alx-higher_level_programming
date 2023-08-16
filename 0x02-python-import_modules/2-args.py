#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    input = argv[1:]
    length = len(input)
    print("{:d} {:s}{:s}".
          format(length,
                 "arguments" if (length) is not 1 else "argument",
                 "." if (length) is 0 else ":"))
    for index, value in enumerate(input):
        print("{:d}: {:s}".format(index + 1, value))
