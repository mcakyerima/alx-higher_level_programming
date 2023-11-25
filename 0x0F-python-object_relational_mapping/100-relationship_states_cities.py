#!/usr/bin/python3
"""
Create a state named "California" with a city attribute "San Francisco".
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

    # Create a state "California" with a city attribute "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add the state and city to the session
    session.add(new_state)
    session.add(new_city)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
