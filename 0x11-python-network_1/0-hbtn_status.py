#!/usr/bin/python3
# Fetches url status

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        status = r.read()

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
    print("\t- utf8 content: {}".format(status.decode('utf-8')))
