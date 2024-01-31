#!/usr/bin/python3
"""
Value of variable X-Request-Id in headers
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    headers = r.headers
    print(str(headers['X-Request-Id']))
