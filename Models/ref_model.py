#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine('mysql://aanito:4762@localhost/db_ref')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define the Hospital model
class Hospital(Base):
    __tablename__ = 'hospitals'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(200))
    services = Column(String(200))
    
    def __init__(self, name, address, services):
        self.name = name
        self.address = address
        self.services = services

# Create the tables
Base.metadata.create_all(engine)


# Close the session
session.close()
