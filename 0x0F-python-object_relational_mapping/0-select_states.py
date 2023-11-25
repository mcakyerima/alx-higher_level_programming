#!/usr/bin/python3

"""
	Displaying all table valus from the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
	database = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])

    # create cursor to exec queries using SQL
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
