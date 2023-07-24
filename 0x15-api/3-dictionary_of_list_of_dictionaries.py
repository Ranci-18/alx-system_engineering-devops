#!/usr/bin/python3
"""GET module"""
import json
import requests


def json_export_all():
    """function to export data in csv format"""
    data = {}
    lst_dct = []
    url1 = 'https://jsonplaceholder.typicode.com/users/'
    response1 = requests.get(url1)
    if response1.status_code == 200:
        obj1 = json.loads(response1.text)
        for dct in obj1:
            USER_ID = dct['id']
            USERNAME = dct['username']
            url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
                .format(USER_ID)
            response2 = requests.get(url2)
            if response2.status_code == 200:
                obj2 = json.loads(response2.text)
            all_titles = []
            status_to_titles = []
            for dictionary in obj2:
                for key, val in dictionary.items():
                    if key == 'title':
                        all_titles.append(val)
                    if key == 'completed':
                        status_to_titles.append(val)

            for title, status in zip(all_titles, status_to_titles):
                dct = {}
                TASK_TITLE = title
                TASK_COMPLETED_STATUS = status
                dct["username"] = USERNAME
                dct["task"] = TASK_TITLE
                dct["completed"] = TASK_COMPLETED_STATUS
                lst_dct.append(dct)

                data["{}".format(USER_ID)] = lst_dct
                try:
                    with open('todo_all_employees.json', 'w') as json_file:
                        json.dump(data, json_file)
                except Exception:
                    pass


if __name__ == '__main__':
    json_export_all()
