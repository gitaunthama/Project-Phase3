from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base, sessionmaker


# Define the SQLite database
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
    description = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    priority = Column(Integer, nullable=False)


    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', due_date='{self.due_date}', priority={self.priority})"



# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def add_task(title, description, due_date, priority):
    new_task = Task(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
    )
    session.add(new_task)
    session.commit()

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
    query=session.query
    for key, value in filters.items():
        query=query.filter(getattr(Task,key)==value)
    return query.all()          
