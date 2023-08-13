#!/usr/bin/python3
# 6-print_matrix_integer.py
# Lujaja Luvuga

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            print("{:d}".format(matrix[row][val]), end='')
            if val != (len(matrix[row]) - 1):
                print(" ", end='')
        print("")
