#!/usr/bin/python3
# Sends a request to url
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {]".format(response.status_code))
