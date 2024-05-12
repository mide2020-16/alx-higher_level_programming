#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with urlopen(url) as response:
            try:
                headers = response.headers
                req_id = headers.get("X-Request-Id")
                print(req_id)
            except Exception as error:
                pass
