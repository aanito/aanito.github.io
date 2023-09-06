import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Get MySQL account credentials from environmental variables
username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')

# Create SQLAlchemy engine
engine = create_engine(f'mysql://{username}:{password}@localhost/')

# Define declarative base
Base = declarative_base()

# Define association table for many-to-many relationship between hospital and service
hospital_service = Table(
    'hospital_service',
    Base.metadata,
    Column('hospital_id', Integer, ForeignKey('hospital.id')),
    Column('service_id', Integer, ForeignKey('service.id'))
)

# Define Hospital model
class Hospital(Base):
    __tablename__ = 'hospital'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    services = relationship('Service', secondary=hospital_service,
                            back_populates='hospitals')

# Define Service model
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hospitals = relationship('Hospital', secondary=hospital_service,
                             back_populates='services')

if __name__ == '__main__':
    # Create the database if it doesn't already exist
    with engine.connect() as conn:
        query=f'CREATE DATABASE IF NOT EXISTS myhosp_db'
        conn.execute(text(query))
    # engine.execute(f'CREATE DATABASE IF NOT EXISTS myhosp_db')
    
    # Bind the engine to the database
    engine = create_engine(f'mysql://{username}:{password}@localhost/myhosp_db')
    Base.metadata.create_all(engine)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Prompt for hospital details
    num_hospitals = int(input("Enter the number of hospitals: "))
    hospitals = []
    for i in range(num_hospitals):
        print(f"\nHospital {i+1}")
        name = input("Name: ")
        address = input("Address: ")
        hospitals.append(Hospital(name=name, address=address))
        session.add(hospitals[i])
    
    # Prompt for service details
    num_services = int(input("\nEnter the number of services: "))
    services = []
    for i in range(num_services):
        print(f"\nService {i+1}")
        service_name = input("Name: ")
        services.append(Service(name=service_name))
        session.add(services[i])
    
    # Link services to hospitals
    for i in range(num_hospitals):
        print(f"\nSelect services for {hospitals[i].name}:")
        for j in range(num_services):
            choice = input(f"Do you want to add {services[j].name}? (y/n): ")
            if choice.lower() == 'y':
                hospitals[i].services.append(services[j])
    
    # Commit the changes and close the session
    session.commit()
    session.close()