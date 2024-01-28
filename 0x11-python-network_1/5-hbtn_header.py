#!/usr/bin/python3
# Value of variable X-Request-Id in headers
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    header = response.headers
    print(header['X-Request-Id'])
