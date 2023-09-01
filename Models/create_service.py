import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from create_db import create_database

username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST', 'localhost')
port = int(os.environ.get('DB_PORT', '3306'))
db_name = os.environ.get('DB_NAME', 'db_ref')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{host}:{port}' #os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    services = db.relationship('Service', backref='hospital', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

def create_tables():
    db.create_all()
    print("Tables created.")

def drop_tables():
    db.drop_all()
    print("Tables dropped.")

if __name__ == '__main__':
    create_tables()
