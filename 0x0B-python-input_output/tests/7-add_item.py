#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
""" adds all arguents to a python list, and then save them to a file"""


if __name__ == '__main__':
    import sys
    import json
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    my_list = []
    try:
        my_list = load(filename)
    except FileNotFoundError:
        pass
    for a in sys.argv[1:]:
        my_list.append(a)
    save(my_list, filename)
    print(my_list)
