#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT id, name FROM states WHERE BINARY name LIKE 'N%'"
        "ORDER BY id ASC"
    )

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
