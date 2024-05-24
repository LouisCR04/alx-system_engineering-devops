#!/usr/bin/python3
# 2-export_to_JSON.py

import json
import requests
import sys


def gather_data():
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        })

    with open(user_id + '.json', mode='w') as file:
        json.dump({user['id']: tasks}, file)


if __name__ == "__main__":
    gather_data()
