#!/usr/bin/python3
"""
Module: 4-cities_by_state.py
Connects to a MySQL server and displays all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def cities_by_state(username, password, database):
    """
    Displays all cities from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Use execute() to fetch all cities in ascending order by cities.id
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials and database name from command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to list all cities from the database hbtn_0e_4_usa
    cities_by_state(username, password, database)
