#!/usr/bin/python3
"""List commits for the 10 most recent commits made by developers"""

import requests  # type: ignore
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    resp = requests.get(url)
    if resp.status_code == 200:
        commits = resp.json()[:10]
        for commit in commits:
            sha = commit['sha']
            auth_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, auth_name))
    else:
        print("Failed to fetch commits.")
