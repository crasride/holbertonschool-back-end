#!/usr/bin/python3
""" module use urllib or requests api """

from requests import get
from sys import argv


if __name__ == "__main__":

    # First we connect/open/read/loads to the data url users
    url_first = get('https://jsonplaceholder.typicode.com/todos/')
    data_url_first = url_first.json()
    completed = 0
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = []

    # Second we connect/open/read/loads to the data url todos
    url_second = get('https://jsonplaceholder.typicode.com/users/')
    data_url_second = url_second.json()

    for i in data_url_first:
        if i.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if i.get('completed') is True:
                completed += 1
                NUMBER_OF_DONE_TASKS.append(i.get('title'))

    for i in data_url_second:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    # Format the name of the completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        employee, completed, TOTAL_NUMBER_OF_TASKS))

    for NUMBER_OF_DONE_TASKS in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(NUMBER_OF_DONE_TASKS))
