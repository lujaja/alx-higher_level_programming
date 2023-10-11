#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define a function"""
import json


def load_from_json_file(filename):
    """Creates an  object from JSON file.

    Args:
        filename (JSON): file
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
