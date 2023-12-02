#!/usr/bin/python3
"""
Given a URL and an Email as parameter, return a response body in utf-8 format, then print error codes.
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""
import sys
import urllib.request

if__name__ == "__main__":
	try:
		url = sys.argv[1]
		with urllib.request.urlopen(url) as response:
			content = response.read().decode('utf-8')
			print(content)
	except urllib.error.HTTPError as e:
		print("Error code: {}".format(e.code))
