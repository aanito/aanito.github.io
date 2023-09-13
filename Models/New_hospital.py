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
    
    # # list existing services with their id
    # existing_services = session.query(Service).all()
    # print("Existing services:")
    # for service in existing_services:
    #     print(f"ID: {service.id}, Name: {service.name}")

    # prompt for hospital details
    hospitals = []
    while True:
        name = input("Name: ")
        address = input("Address: ")

        # check if hospital already exists
        hospital_exists = session.query(Hospital).filter_by(name=name, address=address).first()
        if hospital_exists:
            print("Hospital already exists. Please enter a different hospital.")
        else:
            hospital = Hospital(name=name, address=address)
            session.add(hospital)
            hospitals.append(hospital)
            break

    # list existing services with their id
    existing_services = session.query(Service).all()
    print("Existing services:")
    for service in existing_services:
        print(f"ID: {service.id}, Name: {service.name}")
    
    # link services to hospital
    for hospital in hospitals:
        print(f"\nSelect services for {hospital.name} (Enter service IDs separated by comma):")
        service_ids = input().split(',')
        for service_id in service_ids:
            service = session.query(Service).filter_by(id=int(service_id)).first()
            if service:
                hospital.services.append(service)
    
    # prompt for service details
    services = []
    while True:
        service_name = input("A new service not in the list\nName: ")

        # check if service already exists
        service_exists = session.query(Service).filter_by(name=service_name).first()
        if service_exists:
            print("Service already exists. Please enter a different service.")
        else:
            service = Service(name=service_name)
            session.add(service)
            services.append(service)
            break

    # commit the changes and close the session
    session.commit()
    session.close()
