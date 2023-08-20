#!/usr/bin/python3
# Lujaja luvuga

def multiple_returns(sentence):
    """function to return tuple with lenth of a strin"""
    if (len(sentence) == 0):
        l = None;
    else:
        l = sentence[0];
    lst = [len(sentence), l]
    return tuple(lst)
