#!/usr/bin/python3
"""
Python script named 4-hbtn_status.py that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # Make the GET request using requests
    response = requests.get(url)

    # Display the body of the response with the required format
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

