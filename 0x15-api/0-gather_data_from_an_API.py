#!/usr/bin/python3
"""
"Returns to-do list information for a given employee ID
"""

import requests
import sys

def get_employee_todo_progress(e_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    e_response = requests.get(f"{base_url}/users/{e_id}")
    if e_response.status_code != 200:
        print(f"Error: Unable to find employee data for ID {e_id}")
        sys.exit(1)
    e_data = e_response.json()
    e_name = e_data['name']

    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/users/{e_id}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Unable to find TODO list for employee ID {e_id}")
        sys.exit(1)
    todos = todos_response.json()

    # Calculate progress
    t_tasks = len(todos)
    d_tasks = sum(1 for todo in todos if todo['completed'])

    # Print progress
    print(f"Employee {e_name} is done with tasks({d_tasks}/{t_tasks}): ")

    # Print completed task titles
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <e_id>")
        sys.exit(1)

    try:
        e_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(e_id)
