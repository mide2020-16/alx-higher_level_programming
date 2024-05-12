#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL"""

import urllib
import sys
import urllib.error

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                resp_body = response.read().decode("utf-8")
                print(resp_body)
        except urllib.error.HTTPError as http_error:
            print("Error code: {}".format(http_error))
