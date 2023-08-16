#!/usr/bin/python3
# Lujaja Luvuga

def search_replace(my_list, search, replace):
    """replaces all occurence of an ellement by another in new list
    """
    """
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)
        else:
            new_list.append(num)

    return (new_list)
    """
    return ([num if num != search else replace for num in my_list])
