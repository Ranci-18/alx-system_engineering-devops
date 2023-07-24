#!/usr/bin/python3
"""GET module"""
import csv
import json
import requests
import sys


def csv_export(employee_id):
    """function to export data in csv format"""
    USER_ID = employee_id
    data = []
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(employee_id)
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    if response1.status_code == 200:
        obj1 = json.loads(response1.text)
        USERNAME = obj1['username']
    if response2.status_code == 200:
        obj2 = json.loads(response2.text)
        all_titles = []
        status_to_titles = []
        for dct in obj2:
            for key, val in dct.items():
                if key == 'title':
                    all_titles.append(val)
                if key == 'completed':
                    status_to_titles.append(val)

    for title, status in zip(all_titles, status_to_titles):
        row_data = [str(USER_ID), str(USERNAME), str(status), str(title)]
        data.append(row_data)

    try:
        with open('{}.csv'.format(USER_ID), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csvwriter.writerows(data)
    except FileExistsError:
        pass


if __name__ == '__main__':
    id = sys.argv[1]
    csv_export(id)
