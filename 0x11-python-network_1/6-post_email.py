#!/usr/bin/python3
"""A script which:
- accepts a URL,
- displays the value after sending a request to the URL
- of the X-Request-Id variable present in the respo's header.
- stores the email in the variable email
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Your email is:", email)
        if email in response.text:
            print(response.text)
    else:
        print(f"Error: {response.status_code}")
