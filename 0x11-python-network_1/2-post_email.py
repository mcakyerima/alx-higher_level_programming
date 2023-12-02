#!/usr/bin/python3
"""
Python script named 2-post_email.py that takes a URL and an email as command-line arguments
sends a POST request to the specified URL with the email as a parameterand displays the body of the
response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
	url = argv[1]
	values = {'email': argv[2]}

	data = urllib.parse.urlencode(values)
	data = data.encode('ascii')
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as response:
		content = response.read().decode('utf-8')
        print("Your email is:", email)
		print(content)
