#!/usr/bin/python3
"""
Accepts URL & Email as params, display response body utf-8, print error codes
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(request.text)
