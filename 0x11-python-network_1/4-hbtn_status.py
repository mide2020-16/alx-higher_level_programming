#!/usr/bin/python3
"""A script that usese the request library to make a request"""

import requests # type: ignore
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as resp:
        print("Body response:")
        print("\t- type: {}".format(type(resp.text)))
        print("\t- content: {}".format(resp.text))
