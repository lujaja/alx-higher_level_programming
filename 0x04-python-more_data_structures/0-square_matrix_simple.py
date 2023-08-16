#!/usr/bin/python3
# Lujaja Luvuga

def square_matrix_simple(matrix=[]):
    """computes the square values of all integers of a matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
