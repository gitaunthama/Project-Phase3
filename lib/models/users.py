# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker

# Define the base class
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)


    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')" 

# Define the SQLite database URL
DATABASE_URL = "sqlite:///tasks.db"

# Create an engine to connect to the database
engine = create_engine(DATABASE_URL, echo=True)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, email):
    new_user = User(
        username=username,
        email=email
    )
    session.add(new_user)
    session.commit()

def get_all_users():
    users=  session.query(User).all()
    return users


users=get_all_users()
if users:
    print("Users:")
    for user in users:
        print(user)
else:
    print("No users found.")  



def filter_users(filter):
    query=session.query(User)
    for key, value in filter.items():
        query=query.filter(getattr(User,key)==value)
    return query.all()
    

