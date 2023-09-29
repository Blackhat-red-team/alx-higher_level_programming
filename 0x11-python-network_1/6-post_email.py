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
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    email_printed = False

    if response.status_code == 200:
        if email in response.text:
            print("Your email is:", email)
            email_printed = True

    if email_printed:
        print(response.text)
    else:
        print("Error: Email not found in the response")