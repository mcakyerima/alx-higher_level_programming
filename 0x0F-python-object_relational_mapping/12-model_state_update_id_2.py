#!/usr/bin/python3
"""
Update state name in the database.

This script updates the name of a state with a given ID in the database.

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
    ./script_name.py root root hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine for the MySQL database
    user, passwd, db = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find and update the state with ID 2 (run script #7 to see the table printed)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
