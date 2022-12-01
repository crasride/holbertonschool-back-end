#!/usr/bin/python3
'''
Script to export data in the CSV format
'''
import csv
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]
    # First we connect archive json to the data url users(user_id)
    First_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    data_user = requests.get(First_url).json()
    data_name = data_user.get('username')

    # Second we conect archive json to the data url todos (user_id)
    Second_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    rest_data_user = requests.get(Second_url).json()

    # creates user_id csv file
    file = user_id + '.csv'
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8', newline='') as f:
        # variable write csv file with delimiters and quoting
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        # Write result in rows
        for todo in rest_data_user:
            result = [user_id, data_name, todo.get('completed'),
                      todo.get('title')]
            writer.writerow(result)
