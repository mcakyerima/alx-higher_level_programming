#!/usr/bin/python3
"""
Accepts a letter pattern as param to be search val of request; print Star War names
usage: ./9-starwars.py [letter pattern to match names]
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    param = {'search': argv[1]}
    request = requests.get(url, params=param)

    matching_actors = request.json()
    print("Number of results: {}".format(matching_actors.get('count')))
    for actor in matching_actors.get('results'):
        print(actor.get('name'))
