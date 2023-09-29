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
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url_data = sys.argv[1]

    try:
        respo = requests.get(url_data)
        respo.raise_for_status()

        email = dict(respo.headers).get("X-Request-Id")
        print(email)
    except requests.exceptions.RequestException as z:
        print("An error occurred while fetching the URL:", z)
        sys.exit(1)
