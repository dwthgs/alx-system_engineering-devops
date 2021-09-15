#!/usr/bin/python3
'''
    this module contains the function export_csv
'''
import csv
import requests
from sys import argv


def export_csv(user_id):
    '''
        returns information for a given employee in CSV format
    '''
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    name = user.get('name')
    filename = user_id + '.csv'
    with open(filename, 'w', newline='') as csv_file:
        tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            tasks.writerow([user_id, user.get('username'),
                           task.get('completed'), task.get('title')])


if __name__ == "__main__":
    export_csv(int(argv[1]))
