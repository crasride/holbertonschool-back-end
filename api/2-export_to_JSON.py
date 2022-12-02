#!/usr/bin/python3
"""
Script to export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]
    # First we connect archive json to the data url users(user_id)
    First_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id)

    data_user = requests.get(First_url).json()

    # store the data in a variable
    data_username = data_user.get('username')

    # Second we conect archive json to the data url todos (user_id)
    Second_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    # store the data in a variable
    rest_data_user = requests.get(Second_url).json()

    dict = {user_id: []}

    # creates user_id json file
    file = user_id + '.json'

    for data in rest_data_user:
        result = {
            'task': data.get('title'),
            'completed': data.get('completed'),
            'username': data_username,
        }
        dict[user_id].append(result)

    # Dump result
    with open(file, 'w') as f:
        json.dump(dict, f)
