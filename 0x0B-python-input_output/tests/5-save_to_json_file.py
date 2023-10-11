#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""define function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to text file, using json represntation

    Args:
        my_obj (object): parameter 1
        filename (json): parameter 2
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
