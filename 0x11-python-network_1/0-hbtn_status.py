#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen
if __name__ == "__main__":
	url = "https://alx-intranet.hbtn.io/status"
	with urlopen(url) as response:
		response = response.read()
		print("Body response:")
		print("\t- type: {}".format(type(response)))
		print("\t- content: {}".format(response))
		print("\t- utf8 content: {}".format(response.decode("utf-8")))
