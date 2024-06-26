#!/usr/bin/python3
"""Gathers data from an API"""

import requests
import sys


def gather_data():
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for tasks in completed:
        print("\t {}".format(tasks))


if __name__ == "__main__":
    gather_data()
