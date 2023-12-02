#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse header
usage: ./5-hbtn_header https://intranet.hbtn.io
"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])
    print(request.headers.get('X-Request-Id'))
