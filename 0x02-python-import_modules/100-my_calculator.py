#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    operand_1 = int(argv[1])
    operator = argv[2]
    operand_2 = int(argv[3])

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](operand_1, operand_2)
    print("{:d} {:s} {:d} = {:d}".format(operand_1, operator, operand_2, result))
