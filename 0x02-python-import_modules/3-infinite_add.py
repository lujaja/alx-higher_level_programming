#!/usr/bin/python3
# Lujaja Luvuga

"""Write a program that prints the result of the addition of all
    arguments
    The output should be the result of the addition of all arguments
    , followed by a new line
    You can cast arguments into integers by using int()
    (you can assume that all arguments can be casted into integers)
    Your code should not be executed when imported
"""
if __name__ == "__main__":
    from sys import argv

    count = (len(argv) - 1)
    add = 0

    if (count == 0):
        print("{:d}".format(count))
    elif (count == 1):
        pass
    else:
        for num in range(1, (count + 1)):
            add += int(argv[num])
        print("{:d}".format(add))
