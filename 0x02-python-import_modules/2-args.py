#!/usr/bin/python3
# Lujaja Luvuga

"""write a program that prints the number of and the list of its arguments
The out put should be:
    number of argument(s) followed by argument (if number is one) or
    arguments (otherwise), followed by
    : (or . if no arguments were passed) followed by
    a new line, followed by (if at least one argument),
    one line per argument
    the position of the argument (starting at 1) followed by :
    followed by the argument value and a new line
"""
if __name__ == "__main__":
    from sys import argv

    count = (len(argv) - 1)

    if (count == 0):
        print("{:d} arguments.".format(count))
    elif (count == 1):
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))

    for a in range(1, (count + 1)):
        print("{:d}: {:s}".format(a, argv[a]))
