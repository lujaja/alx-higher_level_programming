#!/usr/bin/python3
# Fetches status
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    if response.status_code == 200:
        res = response.text
        print("Body response:\n\t- type: {}\n\t- content: {}".format
              (type(res), "ok"))
