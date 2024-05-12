#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request"""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    try:
        resp = requests.post(url, data=data)
        json_obj = resp.json()
        if len(json_obj) == 0:
            print("No result")
        else:
            print(f"[{json_obj['id']}] {json_obj['name']}")
    except Exception as error:
        print("Not a valid JSON")
