#!/usr/bin/python3
"""Takes Github credentials and uses GITHUB API to dispaly id"""

import requests # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        url = "https://api.github.com/user"

        with requests.get(url, auth=(username, password)) as resp:
            if resp.status_code == 200:
                json_obj = resp.json()
                print(json_obj['id'])
            else:
                print(None)
