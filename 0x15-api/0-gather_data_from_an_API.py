#!/usr/bin/python3
"""GET module"""
import json
import requests
import sys


def employee_todo(employee_id):
    """function that sends a request"""
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(employee_id)
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    if response1.status_code == 200:
        obj1 = json.loads(response1.text)
        EMPLOYEE_NAME = obj1['name']
    if response2.status_code == 200:
        obj2 = json.loads(response2.text)
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        tasks_completed = []
        for dct in obj2:
            for key, val in dct.items():
                if key == 'id':
                    TOTAL_NUMBER_OF_TASKS += 1
                if key == 'completed' and val is True:
                    NUMBER_OF_DONE_TASKS += 1
                    tasks_completed.append(dct['title'])
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))
        for TASK_TITLE in tasks_completed:
            print("\t", TASK_TITLE)


if __name__ == '__main__':
    id = sys.argv[1]
    employee_todo(id)
