#!/usr/bin/python3
"""
Display the value of X-Request-Id
"""
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        print(response.headers['X-Request-Id'])
