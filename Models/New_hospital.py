import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Models.create_db import create_database

# define the hospitals table using SQLAlchemy ORM
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hospital(Base):
    __tablename__ = 'hospital'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    address = sqlalchemy.Column(sqlalchemy.String(255))
    service = sqlalchemy.Column(sqlalchemy.String(255))

# create the table if it doesn't exist
engine, base = create_database('db_ref')
base.metadata.create_all(engine)

# create a session to interact with the database
def create_session(engine):
    session = sessionmaker(bind=engine)
    return session()

# close the session
def close_session(session):
    session.close()

# prompt the user to enter hospital details
name = input("Enter hospital name: ")
address = input("Enter hospital address: ")

# create and add a new hospital entry
hospital = Hospital(name=name, address=address)
session = create_session(engine)
session.add(hospital)
session.commit()

# close the session
close_session(session)