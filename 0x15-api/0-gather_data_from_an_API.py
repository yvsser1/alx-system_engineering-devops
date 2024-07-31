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

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print(f"Error: Unable to fetch users data")
        sys.exit(1)
    users = users_response.json()

    # Find the employee by ID
    employee = next((user for user in users if user.get('id') == employee_id), None)
    if not employee:
        print(f"Error: Employee with ID {employee_id} not found")
        sys.exit(1)
    employee_name = employee.get('name')

    # Fetch all todos
    todos_response = requests.get(f"{base_url}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list")
        sys.exit(1)
    todos = todos_response.json()

    # Filter todos for the specific employee
    employee_todos = [todo for todo in todos if todo.get('userId') == employee_id]

    total_tasks = len(employee_todos)
    completed_tasks = sum(1 for todo in employee_todos if todo.get('completed', False))

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for todo in employee_todos:
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
