#!/usr/bin/python3
""" 0-subs.py - Gets no. of subs for a reddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns no. of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux: api-advanced:V2.0 (by u/random)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
