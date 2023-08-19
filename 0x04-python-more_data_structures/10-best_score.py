#!/usr/bin/python3
# Lujaja Luvuga

def best_score(a_dictionary):
    """return a key with the biggest interger value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key_list = list(a_dictionary.keys())
    mx = a_dictionary[key_list[0]]
    for k, v in a_dictionary.items():
        if v > mx:
            mx = v
            key_list = k

    return (key_list)
