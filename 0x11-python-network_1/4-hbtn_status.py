#!/usr/bin/python3
"""
Fetches status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    if r.status_code == 200:
        print("Body response:\n\t- type: {}\n\t- content: {}".format
              (type(str(r)), r.text))
