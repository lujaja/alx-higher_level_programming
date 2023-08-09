#!/usr/bin/python3
# Lujaja Luvuga

def remove_char_at(str, n):
    """ Function to create a copy of the string removing
    character at position n

    not the pythion way, the "C array indeX"
    You are not allowd to import any module
    You dont need to understand __import__
    """
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
