#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """print number from 1 to 100 separated by space

    For multiples of three print Fizz
    For multiples of five print Buzz
    For multiples of both three and five print FizzBuzz
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end='')
        elif num % 3 == 0:
            print("Fizz ", end='')
        elif num % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(num), end='')
