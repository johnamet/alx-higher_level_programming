#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the
decoded UTF-8 body of the response.
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """Sends a POST request to the specified URL with the given email as a parameter.

    Args:
        url (str): The URL to send the request to.
        email (str): The email address to send in the POST request.

    Returns:
        str: The decoded body of the response (UTF-8), or None if an error occurs.
    """

    encoded_data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:  # Check for successful response
                return response.read().decode("utf-8")
            else:
                print(f"Error: Server returned status code {response.status}")
                return None
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter URL: ")
    email = input("Enter email: ")

    response_body = send_post_request(url, email)

    if response_body:
        print("Response body:", response_body)
    else:
        print("An error occurred while sending the request.")
