from sqlalchemy import create_engine, Column, Integer, String, Date,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from models import Session
from sqlalchemy.ext.declarative import declarative_base
from models.users import User

# Define the SQLite database URL
DATABASE_URL = "sqlite:///tasks.db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the Task model
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    priority = Column(Integer)

    
    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', due_date='{self.due_date}', priority={self.priority})"

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def add_task(title, description, due_date, priority):
    try:
        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )
        session.add(new_task)
        session.commit()
        print("Task added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Failed to add task: {str(e)}")

def get_all_tasks():
    tasks = session.query(Task).all()
    return tasks

tasks = get_all_tasks()
if tasks:
    print("Tasks:")
    for task in tasks:
        print(task)
else:
    print("No tasks found.")

def filter_tasks(filters):
    query = session.query(Task)
    for key, value in filters.items():
        query = query.filter(getattr(Task, key) == value)
    filtered_tasks = query.all()
    if not filtered_tasks:
        print("No tasks found with the given criteria.")
    return filtered_tasks

