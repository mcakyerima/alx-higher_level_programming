#!/usr/bin/python3
"""
Accepts a  repository and owner name as params, then use Github
API to list user's last 10 commits
usage: ./100-github_commits.py [github_repo] [github_owner]
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    request = requests.get(url)
    commits_count = request.json()
    for commit in commits_count[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
