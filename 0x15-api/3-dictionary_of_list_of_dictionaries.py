#!/usr/bin/python3
# 3-dictionary_of_list_of_dictionaries.py
"""Records all tasks from all employees"""

import json
import requests


def gather_data():
    """Records employees tasks"""
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users = requests.get(url + "users").json()

    # Initialize an empty dictionary to hold all tasks
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch tasks for the current user
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        # Prepare the list of tasks for the current user
        tasks = []
        for todo in todos:
            tasks.append({
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            })

        # Add the user's tasks to the main dictionary
        all_tasks[user_id] = tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    gather_data()
