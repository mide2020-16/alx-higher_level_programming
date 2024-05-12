#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST request"""

import urllib
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email_addr = sys.argv[2]
        data = {"email": email_addr}
        value = urllib.parse.urlencode(data).encode("utf-8")
        req_obj = urllib.request.Request(url, data=value, method="POST")

        with urllib.request.urlopen(req_obj) as response:
            resp_read = response.read()
            resp_str = resp_read.decode("utf-8")
            print(resp_str)
