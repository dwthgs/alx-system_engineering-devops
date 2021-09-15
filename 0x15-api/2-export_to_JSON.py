#!/usr/bin/python3
'''
    this module contains the function export_json
'''
import json
import requests
from sys import argv


def export_json(user_id):
    '''
        returns information for a given employee in JSON format
    '''
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    name = user.get('username')
    filename = user_id + '.json'
    all_tasks = []
    for task in todo:
        current = {}
        current['task'] = task.get('title')
        current['completed'] = task.get('completed')
        current['username'] = name
        all_tasks.append(current)
    json_tasks = {}
    json_tasks[user_id] = all_tasks
    with open(filename, 'w') as json_file:
        json.dump(json_tasks, json_file)


if __name__ == "__main__":
    export_json(int(argv[1]))
