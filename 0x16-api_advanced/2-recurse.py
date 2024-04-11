#!/usr/bin/python3
"""
    2-recurse.py
    Queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list containing the titles of all hot articles for a given sub
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux: api-advanced:V2.0 (by u/random)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
