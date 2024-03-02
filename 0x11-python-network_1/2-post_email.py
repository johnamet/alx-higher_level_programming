#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


def post_email(email, url):
    """
    Sends a POST request to the passed URL with the email as a parameter
    :param email: The email address passed
    :param url: The url to post the email to
    :return: The body of the response
    """
    values = {'email': email}
    headers = {'User-Agent': 'Mozilla/5'}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)

    with urllib.request.urlopen(req) as response:
        return response.read()


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    res = post_email(email, url)

    print(res)
