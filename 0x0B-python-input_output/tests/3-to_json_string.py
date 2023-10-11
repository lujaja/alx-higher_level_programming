#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define to_json_string function"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj (object): parameter 1
    """
    return json.dumps(my_obj)
