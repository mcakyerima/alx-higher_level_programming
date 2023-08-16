#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    command_line_arguments = sys.argv
    if len(command_line_arguments) > 1:
        for i in range(1, len(command_line_arguments)):
            total_sum += int(command_line_arguments[i])
    print("{:d}".format(total_sum))
