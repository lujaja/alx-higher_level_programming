#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as r:
        status = r.read()

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
    print("\t- utf8 content: {}".format(status.decode('utf-8')))
