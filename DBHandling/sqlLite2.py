from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database model using SQLAlchemy ORM
Base = declarative_base()


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    begin_date = Column(Date)
    end_date = Column(Date)


# Create the database connection
def create_connection(db_url):
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)  # Create tables
    Session = sessionmaker(bind=engine)
    return Session()


def insert_data(session, name, begin_date, end_date):
    new_project = Project(name=name, begin_date=begin_date, end_date=end_date)
    session.add(new_project)
    session.commit()
    print(f"Inserted Project with ID: {new_project.id}")
    return new_project.id


def fetch_data(session):
    projects = session.query(Project).all()
    for project in projects:
        print(project.id, project.name, project.begin_date, project.end_date)


def update_data(session, project_id, new_end_date):
    project = session.query(Project).filter(Project.id == project_id).first()
    if project:
        project.end_date = new_end_date
        session.commit()
        print(f"Updated Project ID {project_id}")


def delete_data(session, project_id):
    project = session.query(Project).filter(Project.id == project_id).first()
    if project:
        session.delete(project)
        session.commit()
        print(f"Deleted Project ID {project_id}")


def main():
    database_url = "sqlite:///pythonsqlite.db"  # SQLite URL format

    # Create a session
    session = create_connection(database_url)

    # Insert data
    project_id = insert_data(
        session, "Cool App with SQLite & Python", "2021-01-01", "2021-01-30"
    )

    # Fetch data
    print("Initial data:")
    fetch_data(session)

    # Update data
    update_data(session, project_id, "2021-02-01")

    # Fetch data after update
    print("Data after update:")
    fetch_data(session)

    # Delete data
    delete_data(session, project_id)

    # Fetch data after delete
    print("Data after delete:")
    fetch_data(session)


if __name__ == "__main__":
    main()
