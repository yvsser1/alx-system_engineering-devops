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

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        sys.exit(1)
    user_data = user_response.json()
    e_name = user_data.get('name')

    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch list for employee ID {employee_id}")
        sys.exit(1)
    todos = todos_response.json()

    t_tasks = len(todos)
    c_tasks = sum(1 for todo in todos if todo.get('completed', False))

    # Also print to console
    print(f"Employee {e_name} is done with tasks({c_tasks}/{t_tasks}): ")
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
