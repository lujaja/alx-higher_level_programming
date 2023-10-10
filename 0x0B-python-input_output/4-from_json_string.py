#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define from_json_string finction"""
import json


def from_json_string(my_str):
    """Object representation by json string.

    Args:
        my_str (object): parameter 1
    """
    return json.dumps(my_str)

