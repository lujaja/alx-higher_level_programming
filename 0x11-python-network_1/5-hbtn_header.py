#!/usr/bin/python3
"""
Value of variable X-Request-Id in headers
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code == 200:
        for key, value in r.headers.items():
            if key == "X-Request-Id":
                print("{}".format(value))
                break
    else:
        print(f"Error: {r.status_code} - {r.reason}")
