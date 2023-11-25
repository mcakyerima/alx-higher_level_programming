#!/usr/bin/python3
"""
Module: 5-filter_cities.py
Connects to a MySQL server and lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a given state from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state to filter cities.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Use execute() to fetch all cities in ascending order by cities.id
    query = "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ') \
             FROM cities JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s"
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Display the results
    if result:
        print(result)

    # Close the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials, database name, and state name from command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the function to list all cities of the given state from the database hbtn_0e_4_usa
    filter_cities_by_state(username, password, database, state_name)
