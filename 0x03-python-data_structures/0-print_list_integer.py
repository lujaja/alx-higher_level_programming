#!/use/bin/python3
# 0-print_list_integer.py
# Lujaja Luvuga

def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    if isinstance(my_list, list):
        for num in range(len(my_list)):
            print("{:d}".format(my_list[num]))
