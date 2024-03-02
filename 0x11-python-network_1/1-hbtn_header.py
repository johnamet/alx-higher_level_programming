#!/usr/bin/python3
"""The script shows how to:
- take in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib.request import Request, urlopen


def get_request_id(_url):
    """
  Fetches the X-Request-Id value from the header of a response to the given URL.

  Args:
      _url: The URL to send the request to.

  Returns:
      The value of the X-Request-Id header, or None if it's not found.
  """

    try:
        # Create a request object with a custom User-Agent header
        req = Request(_url, headers={"User-Agent": "MyCoolScript"})

        # Send the request and open the response in a with statement
        with urlopen(req) as response:
            # Get the headers as a dictionary
            headers = dict(response.headers)

            # Return the X-Request-Id value if it exists, otherwise None
            return headers.get("X-Request-Id")

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Get the URL from the command line, even if incorrect arguments are provided
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com"  # Default URL

    # Get the X-Request-Id and print it (if found)
    request_id = get_request_id(url)
    if request_id:
        print(request_id)
