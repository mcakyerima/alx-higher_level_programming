#!/usr/bin/python3
"""
This script retrieves State objects containing the letter 'a' from a MySQL database using Python.

Usage:
    ./script_name.py <username> <password> <database>

Parameters:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database.

Requirements:
    - The script requires the model_state module containing the State class and Base instance.
    - The sqlalchemy module must be installed.

Example:
    ./script_name.py root root hbtn_0e_0_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine for the MySQL database
    user, passwd, db = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State instances in the database containing the letter 'a'
    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
