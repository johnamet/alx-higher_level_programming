#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the
decoded UTF-8 body of the response.
"""
import sys
import urllib.parse
import urllib.request


def post_email(email, url):
    """
    Sends a POST request to the URL with the email
    as a parameter in JSON format.

    Args:
        email (str): The email address to be sent.
        url (str): The URL to send the POST request to.

    Returns:
        bytes: The decoded UTF-8 response body, if successful.
        None: Otherwise, if an error occurs.
    """

    try:
        # Build data as JSON for better compatibility with servers
        data = ({'email': email}.encode('utf-8'))
        headers = {'Content-Type': 'application/json',
                   'User-Agent': 'Mozilla/5'}

        # Create and send the request using a with statement
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')  # Decode response in UTF-8
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Handle potential errors gracefully without checking argument types
    try:
        url = sys.argv[1]
        email = sys.argv[2]
        response = post_email(email, url)
        if response:  # Check if response exists (error handling)
            print(response)
        else:
            print("Error occurred during request.")
    except IndexError:
        print("Error: Missing arguments."
              "Please provide a URL and an email address.")
    except Exception as e:
        print(f"Unexpected error: {e}")
