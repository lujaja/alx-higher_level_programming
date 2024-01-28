#!/usr/bin/python3
# Sendt a request to url and displays the body
from urllib.request import urlopen
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode("utf-8")
            print("{}".format(body))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error connecting to the server: {}".format(e.reason))
