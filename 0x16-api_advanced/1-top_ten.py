#!/usr/bin/python3
""" 1-top_ten.py - Top 10 hot posts for a sub """

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given sub"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux: api-advanced:v1.0 (by u/random)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(i.get("data").get("title")) for i in results.get("children")]
