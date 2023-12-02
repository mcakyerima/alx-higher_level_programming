#!/usr/bin/python3
"""
Accepts a username and pwd as params, get your id from Github api usage: ./10-my_github.py [github_username] [github_pwd]
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    credentials = HTTPBasicAuth(argv[1], argv[2])
    request = requests.get(url, auth=credentials)
    print(request.json().get('id'))
