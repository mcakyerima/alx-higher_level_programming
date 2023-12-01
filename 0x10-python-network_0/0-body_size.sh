#!/bin/bash

# Bash Script that takes in a URL, sends a request to the URL and displays the size of the body of respose
curl -sI $1 | grep -i Content-Length | cut -d " " -f 2
