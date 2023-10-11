#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Class_to+json function definition"""


def class_to_json(obj):
    """Return dictionary description with siple data structure.

    Args:
        obj (object): function argument.
    Return:
        dictionary description for json serialization of object
    """
    return obj.__dict__
