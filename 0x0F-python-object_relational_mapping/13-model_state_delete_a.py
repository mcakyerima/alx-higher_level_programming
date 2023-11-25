#!/usr/bin/python3
"""
Deletes rows from the 'states' table with names containing the letter 'a'.
Parameters given to the script: username, password, database
"""

from sys import argv
from model_state import Base, State
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

    # Find all states with names containing 'a' and delete them
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit changes and close the session
    session.commit()
    session.close()
