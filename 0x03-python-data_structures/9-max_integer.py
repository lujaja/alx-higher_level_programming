#!/usr/bin/python3
# Lujaja Luvuga

def max_integer(my_list=[]):
    if isinstance(my_list, list):
        num = my_list[0]
        for i in range(len(my_list)):
            if num < my_list[i]:
                num = my_list[i]
        return num
