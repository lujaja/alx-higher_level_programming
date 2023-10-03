#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>


def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    l = 1
    while l < len(list):
        if list[l] > result:
            result = list[l]
        l += 1
    return result
