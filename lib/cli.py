# cli.py
from operations import create_user, read_users, update_user, delete_user
from operations import create_project, read_projects, update_project, delete_project
from operations import create_task, read_tasks, update_task, delete_task

def main():
    while True:
        print("\nTask Management System")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Add Project")
        print("6. View Projects")
        print("7. Update Project")
        print("8. Delete Project")
        print("9. Add Task")
        print("10. View Tasks")
        print("11. Update Task")
        print("12. Delete Task")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            update_user_cli()
        elif choice == "4":
            delete_user_cli()
        elif choice == "5":
            add_project()
        elif choice == "6":
            view_projects()
        elif choice == "7":
            update_project_cli()
        elif choice == "8":
            delete_project_cli()
        elif choice == "9":
            add_task()
        elif choice == "10":
            view_tasks()
        elif choice == "11":
            update_task_cli()
        elif choice == "12":
            delete_task_cli()
        elif choice == "0":
            break
        else:
            print("Invalid choice, please try again.")

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    create_user(username, email)
    print("User added successfully!")

def view_users():
    users = read_users()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    else:
        print("No users found.")

def update_user_cli():
    user_id = int(input("Enter user ID: "))
    username = input("Enter new username: ")
    email = input("Enter new email: ")
    update_user(user_id, username, email)
    print("User updated successfully!")

def delete_user_cli():
    user_id = int(input("Enter user ID to delete: "))
    delete_user(user_id)
    print("User deleted successfully!")

def add_project():
    name = input("Enter project name: ")
    description = input("Enter project description: ")
    create_project(name, description)
    print("Project added successfully!")

def view_projects():
    projects = read_projects()
    if projects:
        print("\nProjects:")
        for project in projects:
            print(f"ID: {project[0]}, Name: {project[1]}, Description: {project[2]}")
    else:
        print("No projects found.")

def update_project_cli():
    project_id = int(input("Enter project ID: "))
    name = input("Enter new project name: ")
    description = input("Enter new project description: ")
    update_project(project_id, name, description)
    print("Project updated successfully!")

def delete_project_cli():
    project_id = int(input("Enter project ID to delete: "))
    delete_project(project_id)
    print("Project deleted successfully!")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = int(input("Enter priority (1-5): "))
    user_id = int(input("Enter user ID assigned to the task: "))
    project_id = int(input("Enter project ID for the task: "))
    create_task(title, description, due_date, priority, user_id, project_id)
    print("Task added successfully!")

def view_tasks():
    tasks = read_tasks()
    if tasks:
        print("\nTasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due Date: {task[3]}, Priority: {task[4]}, User ID: {task[5]}, Project ID: {task[6]}")
    else:
        print("No tasks found.")

def update_task_cli():
    task_id = int(input("Enter task ID: "))
    title = input("Enter new task title: ")
    description = input("Enter new task description: ")
    due_date = input("Enter new due date (YYYY-MM-DD): ")
    priority = int(input("Enter new priority (1-5): "))
    user_id = int(input("Enter new user ID assigned to the task: "))
    project_id = int(input("Enter new project ID for the task: "))
    update_task(task_id, title, description, due_date, priority, user_id, project_id)
    print("Task updated successfully!")

def delete_task_cli():
    task_id = int(input("Enter task ID to delete: "))
    delete_task(task_id)
    print("Task deleted successfully!")

if __name__ == "__main__":
    main()
