#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
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
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command-line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to list states
    list_states(username, password, database)

