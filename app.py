import os
from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
# from sqlalchemy import create_engine

username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST', 'localhost')
port = int(os.environ.get('DB_PORT', '3306'))
db_name = os.environ.get('DB_NAME', 'db_ref')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{host}/{db_name}'

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
    # Add more columns as required by your hospital table

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/setup', methods=['GET'])
def setup():
    return render_template('setup.html')

@app.route('/hospitals', methods=['GET'])
def search_hospitals():
    
    query = request.args.get('query', '')
    hospitals = Hospital.query.filter(Hospital.name.ilike(f'%{query}%')).all()
    results = [{'id': hospital.id, 'name': hospital.name} for hospital in hospitals]
    return jsonify(results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)