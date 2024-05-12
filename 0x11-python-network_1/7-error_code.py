#!/usr/bin/python3
"""A script that makes a request and checks the status code."""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with requests.get(url) as resp:
            if resp.status_code < 400:
                print(resp.text)
            else:
                print(f"Erro code: {resp.status_code}")
