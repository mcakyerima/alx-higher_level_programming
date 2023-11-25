#!/usr/bin/python3
"""
This script returns the state ID for a given state name from a MySQL database in a SQL injection-free manner.

Usage:
    ./script_name.py <username> <password> <database> <state_name>

Parameters:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database.
    state_name (str): Name of the state to match.

Requirements:
    - The script requires the model_state module containing the State class and Base instance.
    - The sqlalchemy module must be installed.

Example:
    ./script_name.py root root hbtn_0e_0_usa "New York"
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine for the MySQL database
    user, passwd, db, state_name = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State instance in the database for the given state name
    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
