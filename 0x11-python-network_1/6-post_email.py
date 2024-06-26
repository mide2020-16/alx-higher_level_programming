#!/usr/bin/python3
"""A script that makes a post request with requests library"""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email_addr = sys.argv[2]
        resp = requests.post(url, data={"email": email_addr})
        print(resp.text)
