from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from .import Session 

# Define the SQLite database URL
DATABASE_URL = "sqlite:///tasks.db"

# Create an engine to connect to the database
engine = create_engine(DATABASE_URL, echo=True)

# Create a session maker
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)


     
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

# Create the tables in the database
Base.metadata.create_all(engine)

def add_user(username, email):
    new_user = User(
        username=username,
        email=email
    )
    session.add(new_user)
    session.commit()

def get_all_users():
    return session.query(User).all()

def filter_users(**kwargs):
    query = session.query(User)
    for key, value in kwargs.items():
        query = query.filter(getattr(User, key) == value)
    return query.all()

# Testing the functions
if __name__ == "__main__":
    # Add a user
    add_user("john", "john@example.com")

    # Retrieve all users
    users = get_all_users()
    if users:
        print("Users:")
        for user in users:
            print(user)
    else:
        print("No users found.")

    # Filter users
    filtered_users = filter_users(username='john')
    if filtered_users:
        print("\nFiltered Users:")
        for user in filtered_users:
            print(user)
    else:
        print("No users matching the filter criteria.")
