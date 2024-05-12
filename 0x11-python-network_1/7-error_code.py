#!/usr/bin/python3
"""A script that makes a request and checks the status code."""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        resp = requests.get(url)
        if resp.status_code < 400:
            print(resp.content)
        else:
            print(f"Error code: {resp.status_code}")
