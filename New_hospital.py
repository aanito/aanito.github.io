import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from Models.create_db import create_database
from sqlalchemy.ext.declarative import declarative_base

username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST', 'localhost')
port = int(os.environ.get('DB_PORT', '3306'))
db_name = os.environ.get('DB_NAME', 'db_ref')

SQLALCHEMY_DATABASE_URI = f'mysql://{username}:{password}@{host}:{port}/{db_name}'

Base = declarative_base()

class Hospital(base):
    __tablename__ = 'hospital'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    address = sqlalchemy.Column(sqlalchemy.String(255))
    service = sqlalchemy.Column(sqlalchemy.String(255))

engine, base = create_database(SQLALCHEMY_DATABASE_URI)
base.metadata.create_all(engine)

def create_session(engine):
    session = sessionmaker(bind=engine)
    return session()

def close_session(session):
    session.close()

name = input("enter hospital name: ")
address = input("enter hospital address: ")
services = input("enter hospital services (comma-separated): ")

hospital = Hospital(name=name, address=address, service=services)
session = create_session(engine)
session.add(hospital)
session.commit()

close_session(session)