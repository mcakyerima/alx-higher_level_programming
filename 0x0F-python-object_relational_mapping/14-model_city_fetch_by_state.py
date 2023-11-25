#!/usr/bin/python3
"""
Returns information about all cities from the database via Python.
Parameters given to the script: username, password, database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Establish a connection to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)

    # Create metadata and session objects
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query multiple tables in the database and print information
    for result in session.query(State.name, City.id, City.name).filter(State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(result[0], result[1], result[2]))

    # Close the session
    session.close()
