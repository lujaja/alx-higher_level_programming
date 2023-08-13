#!/use/bin/python3
# Lujaja Luvuga

def print_list_integer(my_list=[]):
    """write a function that prints all integers of a list
    one int per line
    dont import any module
    assume the list only contains ints
    you are not allowed to cast integers into string
    you have to use str.format() to print integers
    """
    for num in my_list:
        print("{:d}".format(num))
