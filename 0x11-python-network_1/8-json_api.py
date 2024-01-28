#!/usr/bin/python3
# Post requests
from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(argv) > 1:
        letter = argv[1]

    payload = {'q': letter}
    response = requests.get(url, data=payload)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
