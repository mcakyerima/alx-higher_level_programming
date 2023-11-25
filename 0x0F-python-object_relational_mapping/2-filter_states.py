#!/usr/bin/python3
"""
Module: 2-filter_states.py
Connects to a MySQL server and displays values in the states table based on user input.
"""

import MySQLdb
import sys


def filter_states_by_user_input(username, password, database, state_name):
    """
    Displays values in the states table based on user input.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): State name to search for.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials and state name from command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the function to filter and list states by user input
    filter_states_by_user_input(username, password, database, state_name)
