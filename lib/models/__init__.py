import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the SQLite database URL
DATABASE_URL = "sqlite:///tasks.db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

from .tasks import Task
from .users import User

