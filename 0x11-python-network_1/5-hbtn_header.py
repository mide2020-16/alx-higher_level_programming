#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL"""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with requests.get(url) as resp:
            resp_headers = resp.headers
            req_id = resp_headers.get("X-Request-Id")
            print(req_id)
