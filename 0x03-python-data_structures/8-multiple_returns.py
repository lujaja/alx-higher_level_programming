#!/usr/bin/python3
# Lujaja luvuga

def multiple_returns(sentence):
    """function to return tuple with lenth of a strin"""
    if (len(sentence) == 0):
        return (None)
    lst = [len(sentence), sentence[0]]
    return tuple(lst)
