#!/usr/bin/python3
"""
Use table relationships to access and print city and state information.
Parameters given to the script: username, password, database.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Create an engine for the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use table relationships to access and print city and state information
    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
