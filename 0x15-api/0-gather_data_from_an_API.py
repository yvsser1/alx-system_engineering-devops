#!/usr/bin/python3
"""
This script retrieves and displays an employee's TODO list progress
using the JSONPlaceholder API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")
        sys.exit(1)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name', 'Unknown')

    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        sys.exit(1)
    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo.get('completed', False))

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for todo in todos:
        if todo.get('completed', False):
            print(f"\t {todo.get('title', 'Untitled task')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
