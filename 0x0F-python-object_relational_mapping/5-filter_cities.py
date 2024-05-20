#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC""", (state_name,))

    cities = cursor.fetchall()

    requested_cities = [city[0] for city in cities]
    print(", ".join(requested_cities))

    cursor.close()
    db.close()
