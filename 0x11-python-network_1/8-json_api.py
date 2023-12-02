#!/usr/bin/python3
"""
Accepts a  letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    request = requests.post(url, data=data)

    try:
        dic = request.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
