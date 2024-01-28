#!/usr/bin/python3
# Post request
from sys import argv
import requests

if __name__ == "__main__":
    payload = {'email': argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response.text)
