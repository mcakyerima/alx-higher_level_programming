#!/usr/bin/python3
"""
This script retrieves the first State object from a MySQL database using Python.

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

    # Query the first State instance in the database
    first_instance = session.query(State).order_by(State.id).first()

    # Print the result or indicate if nothing is found
    if first_instance:
        print(f"{first_instance.id}: {first_instance.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
