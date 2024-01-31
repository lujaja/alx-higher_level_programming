#!/usr/bin/python3
"""
Sends a post request
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urlencode(value).encode('ascii')
    with urlopen(url, data) as response:
        body = response.read().decode("utf-8")
        print("{}".format(body))
