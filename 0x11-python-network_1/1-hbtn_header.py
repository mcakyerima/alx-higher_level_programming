#!/usr/bin/python3

"""
Python script named 1-hbtn_header.py that takes a URL
as a command-line argument, sends an HTTP request, and displays the value of the X-Request-Id variable found in the response
header
"""
import sys
import urllib.request

if __name__ == '__main__':
	url = urllib.request.Request(sys.argv[1])

	with urllib.request.urlopen(url) as response:
		x_request_id = response.headers.get('X-Request-Id')
		print(x_request_id)
