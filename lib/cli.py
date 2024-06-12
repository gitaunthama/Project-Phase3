from models.tasks import add_task, get_all_tasks, filter_tasks
from models.users import add_user, get_all_users, filter_users
from models.workproject import add_project, get_all_projects, filter_projects
from helpers import exit_program
from datetime import datetime

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_task_app()
        elif choice == "2":
            add_user_app()
        elif choice == "3":
            add_project_app()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            view_projects()
        elif choice == "6":
            view_users()
        elif choice == "7":
            filter_menu()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add task")
    print("2. Add user")
    print("3. Add project")
    print("4. View all tasks")
    print("5. View all projects")
    print("6. View all users")
    print("7. Filter data")
    print()

def filter_menu():
    print("Filter options:")
    print("1. Filter tasks")
    print("2. Filter users")
    print("3. Filter projects")
    choice = input("> ")

    if choice == "1":
        filter_tasks_app()
    elif choice == "2":
        filter_users_app()
    elif choice == "3":
        filter_projects_app()
    else:
        print("Invalid choice")

def filter_tasks_app():
    print("Enter filter criteria for tasks (leave blank to skip a criterion):")
    title = input("Title: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    priority = input("Priority (1 for high, 2 for medium, 3 for low): ")

    filters = {}
    if title:
        filters['title'] = title
    if due_date and validate_date(due_date):
        filters['due_date'] = datetime.strptime(due_date, "%Y-%m-%d").date()
    if priority and priority.isdigit() and int(priority) in [1, 2, 3]:
        filters['priority'] = int(priority)

    tasks = filter_tasks(filters)
    if tasks:
        print("Filtered tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks found with the given criteria.")

def filter_users_app():
    print("Enter filter criteria for users (leave blank to skip a criterion):")
    username = input("Username: ")
    email = input("Email: ")

    filters = {}
    if username:
        filters['username'] = username
    if email:
        filters['email'] = email

    users = filter_users(filters)
    if users:
        print("Filtered users:")
        for user in users:
            print(user)
    else:
        print("No users found with the given criteria.")

def filter_projects_app():
    print("Enter filter criteria for projects (leave blank to skip a criterion):")
    name = input("Project name: ")

    filters = {}
    if name:
        filters['name'] = name

    projects = filter_projects(filters)
    if projects:
        print("Filtered projects:")
        for project in projects:
            print(project)
    else:
        print("No projects found with the given criteria.")

def add_task_app():
    print("Enter task details:")
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    priority = input("Priority (1 for high, 2 for medium, 3 for low): ")

    if not title:
        print("Title is required.")
        return

    due_date_obj = None
    if due_date:
        if not validate_date(due_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()

    if not priority or not priority.isdigit() or int(priority) not in [1, 2, 3]:
        print("Invalid priority. Please enter 1 for high, 2 for medium, or 3 for low.")
        return

    priority_int = int(priority)
    add_task(title, description, due_date_obj, priority_int)
    print("Task added successfully.")

def add_user_app():
    print("Enter user details:")
    username = input("Username: ")
    email = input("Email: ")

    if not username:
        print("Username is required.")
        return

    if not email:
        print("Email is required.")
        return

    add_user(username, email)
    print("User added successfully.")

def add_project_app():
    print("Enter project details:")
    name = input("Project name: ")
    description = input("Project description: ")

    if not name:
        print("Project name is required.")
        return

    add_project(name, description)
    print("Project added successfully.")

def view_tasks():
    tasks = get_all_tasks()
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def view_users():
    users = get_all_users()
    if users:
        print("Users:")
        for user in users:
            print(user)
    else:
        print("No users found.")

def view_projects():
    projects = get_all_projects()
    if projects:
        print("Projects:")
        for project in projects:
            print(project)
    else:
        print("No projects found.")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
