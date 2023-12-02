#!/usr/bin/python3
"""
Python script using urllib to fetch the status from the given
URL and display the required information
"""
import urllib.request

if __name__ == "__main__":
	url = 'https://alx-intranet.hbtn.io/status'
	with urllib.request.urlopen(url) as response:
		content = response.read()
		utf8_content = content.decode('utf-8')

		print("Body response:")
		print("\t- type:", type(content))
		print("\t- content:", content)
		print("\t- utf8 content:", utf8_content)
