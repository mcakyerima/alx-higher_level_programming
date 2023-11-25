#!/usr/bin/python3
"""
Module: 0-select_states.py
Connects to a MySQL server and lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Lists all states from the specified database.

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

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

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

    # Get MySQL credentials from command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to list states
    list_states(username, password, database)
