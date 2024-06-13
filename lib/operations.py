import sqlite3

# Function to establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    return conn


# Function to create the necessary tables if they do not already exist
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Create the users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
        ''')

        # Create the projects table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
        ''')

        # Create the tasks table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            due_date TEXT,
            priority INTEGER,
            user_id INTEGER,
            project_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
        ''')

        # Commit the changes to the database
        conn.commit()
        print("Tables created successfully")
    except sqlite3.Error as e:
        # Print any database errors that occur
        print(f"Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

# Function to insert sample data into the tables
def insert_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Insert sample data into users table
        cursor.executemany('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
        ''', [
            ('Alice', 'alice@example.com'),
            ('Bob', 'bob@example.com')
        ])

        # Insert sample data into projects table
        cursor.executemany('''
        INSERT INTO projects (name, description)
        VALUES (?, ?)
        ''', [
            ('Project 1', 'Description of project 1'),
            ('Project 2', 'Description of project 2')
        ])

        # Insert sample data into tasks table
        cursor.executemany('''
        INSERT INTO tasks (title, description, due_date, priority, user_id, project_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', [
            ('Task 1', 'Description of task 1', '2024-07-01', 1, 1, 1),
            ('Task 2', 'Description of task 2', '2024-07-10', 2, 2, 2)
        ])

        # Commit the changes to the database
        conn.commit()
        print("Sample data inserted successfully")
    except sqlite3.Error as e:
        # Print any database errors that occur
        print(f"Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

# Function to create a new user
def create_user(username, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
        ''', (username, email))
        
        conn.commit()
        return cursor.lastrowid  # Return the ID of the new user
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        return None
    finally:
        conn.close()

# Function to read all users
def read_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        conn.close()

# Function to update a user
def update_user(user_id, username, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        UPDATE users
        SET username = ?, email = ?
        WHERE id = ?
        ''', (username, email, user_id))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating user: {e}")
        return False
    finally:
        conn.close()

# Function to delete a user
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")
        return False
    finally:
        conn.close()

# Function to create a new project
def create_project(name, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO projects (name, description)
        VALUES (?, ?)
        ''', (name, description))
        
        conn.commit()
        return cursor.lastrowid  # Return the ID of the new project
    except sqlite3.Error as e:
        print(f"Error creating project: {e}")
        return None
    finally:
        conn.close()

# Function to read all projects
def read_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM projects')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching projects: {e}")
        return []
    finally:
        conn.close()

# Function to update a project
def update_project(project_id, name, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        UPDATE projects
        SET name = ?, description = ?
        WHERE id = ?
        ''', (name, description, project_id))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating project: {e}")
        return False
    finally:
        conn.close()

# Function to delete a project
def delete_project(project_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting project: {e}")
        return False
    finally:
        conn.close()

# Function to create a new task
def create_task(title, description, due_date, priority, user_id, project_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority, user_id, project_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, description, due_date, priority, user_id, project_id))
        
        conn.commit()
        return cursor.lastrowid  # Return the ID of the new task
    except sqlite3.Error as e:
        print(f"Error creating task: {e}")
        return None
    finally:
        conn.close()

# Function to read all tasks
def read_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM tasks')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching tasks: {e}")
        return []
    finally:
        conn.close()

# Function to update a task
def update_task(task_id, title, description, due_date, priority, user_id, project_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?, priority = ?, user_id = ?, project_id = ?
        WHERE id = ?
        ''', (title, description, due_date, priority, user_id, project_id, task_id))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating task: {e}")
        return False
    finally:
        conn.close()

# Function to delete a task
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting task: {e}")
        return False
    finally:
        conn.close()

# Main entry point for testing operations
if __name__ == '__main__':
    # Example usage: Create tables and insert sample data
    create_tables()
    insert_sample_data()
    # Add more testing as needed
