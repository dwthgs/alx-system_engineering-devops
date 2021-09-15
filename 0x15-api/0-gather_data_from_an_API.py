#!/usr/bin/python3
'''
    this module contains the function get_info
'''
import requests
from sys import argv


def get_info(employee_id):
    '''
        returns information for a given employee ID
    '''
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    name = user.get('name')
    done_tasks = []
    done_count = 0
    total_count = 0
    for task in todo:
        total_count += 1
        if task.get('completed'):
            done_tasks.append(task.get('title'))
            done_count += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, done_count, total_count))
    for task in done_tasks:
        print('\t {}'.format(task))


if __name__ == "__main__":
    get_info(int(argv[1]))
