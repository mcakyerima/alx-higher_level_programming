#!/usr/bin/python3
"""
Python script named 2-post_email.py that takes a URL and an email as command-line arguments,
sends a POST request to the specified URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')

    # Create the request object
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and handle the response
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')

    # Display the results
    print("Your email is:", email)
    print(content)
