#!/usr/bin/python3
# 1-export_to_CSV.py

"""Gathers data from an API"""

import requests
import sys
import csv


def gather_data():
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    data = []

    for todo in todos:
        data.append({
            "USER_ID": user['id'],
            "USERNAME": user['username'],
            "TASK_COMPLETED_STATUS": todo['completed'],
            "TASK_TITLE": todo['title']
        })

    with open(user_id + '.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["USER_ID", "USERNAME",
                                "TASK_COMPLETED_STATUS", "TASK_TITLE"],
                                quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    gather_data()
