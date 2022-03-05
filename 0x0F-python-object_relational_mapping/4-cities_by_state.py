#!/usr/bin/python3
"""
This module contains
A script that lists all cities from the database hbtn_0e_4_usa
And it takes three aruments (username, password) for mysql and database name
"""
import MySQLdb
import sys


def main():
    """
    This function shows cities.id, cities.name and states.name
    and I used inner join to join the two tables and SELECT query.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name,
        states.name FROM cities INNER JOIN states ON
        cities.state_id=states.id ORDER BY id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
