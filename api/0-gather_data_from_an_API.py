#!/usr/bin/python3
""" module use urllib or requests api"""
import json
import urllib.request
from sys import argv


# First we connect/open/read/loads to the data url users
url = "https://jsonplaceholder.typicode.com/users/"
Source_url = urllib.request.urlopen(url)
data_url = Source_url.read()
object = json.loads(data_url.decode('utf-8'))

# Now we get the name of the employee
EMPLOYEE_NAME = object[int(argv[1]) - 1]["name"]

# Second we connect/open/read/loads to the data url todos
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
Source_url = urllib.request.urlopen(url)
data_url = Source_url.read()

# Now we get the name of the todo
TOTAL_NUMBER_OF_TASKS = json.loads(data_url.decode('utf-8'))
NUMBER_OF_DONE_TASKS = [i for i in TOTAL_NUMBER_OF_TASKS
                        if i["completed"] is True]

# Format the name of the completed tasks
print("Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)
))
for NUMBER_OF_DONE_TASKS in NUMBER_OF_DONE_TASKS:
    print("\t {}".format(NUMBER_OF_DONE_TASKS["title"]))
