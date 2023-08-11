#!/usr/bin/python3
# Lujaja Luvuga

if __name__ == "__main__":
    """write a program that imports all functions from the file
    calculator_1.py and handles basic operations.

    usage: ./100-my_calculator.py a operator b
        If the number of arguments is not 3, your program has to:
            print Usage: ./100-my_calculator.py <a> <operator> <b>
            folowed by a new line
            exit with value 1
        If the operator is not one of the above:
            print Unknown operator. Available operators: +, -, * and /
            folowed by a new line
            exit with the value 1
    """
    import sys
    from calculator_1 import add, sub, mul, div

    count = (len(sys.argv) - 1)

    if (count != 3):
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)

    op = {"-": sub, "*": mul, "/": div, "+": add}
    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
    sys.exit(0)
