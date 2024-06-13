from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base


# Define the SQLite database
DATABASE_URL = "sqlite:///tasks.db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the Project model
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

   


    def __str__(self):
        return f"Project(id={self.id}, name='{self.name}', description='{self.description}')"

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def add_project(name, description):
    new_project = Project(
        name=name,
        description=description
    )
    session.add(new_project)
    session.commit()

def get_all_projects():
    projects = session.query(Project).all()
    return projects

projects = get_all_projects()
if projects:
    print("Projects:")
    for project in projects:
        print(project)
else:
    print("No projects found.")

def filter_projects(filters):
    query = session.query(Project)
    for key, value in filters.items():
        query = query.filter(getattr(Project, key) == value)
    return query.all()
