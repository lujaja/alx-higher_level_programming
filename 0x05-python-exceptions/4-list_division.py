#!/usr/bin/pyhton3
# 4-list_division.py
# Lujaja Luvuga <jarzcyber@gmail.com>

def list_division(my_list_1, my_list_2, list_length):
    """ Divides Element by element in 2 lists.

    Args:
        my_list_1: argument 1.
        my_list_2: argument 2.
        list_length: argument 3.

    Return:
        New list with all diviaions.
        if elements cant be divided the division result should be 0.
        if element not integer or float print wrong type.
        if divition cant br done print division by zero.
        if one of lists too sshort print out of range.
    """

    new_list = []
    for num in range(list_length):
        try:
            div = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
