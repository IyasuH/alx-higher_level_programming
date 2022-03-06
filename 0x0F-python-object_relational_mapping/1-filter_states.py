#!/usr/bin/python3
"""
A script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
And the script takes 3 aguments mysql username, mysql password
and database name using sys.argv.
"""
import MySQLdb
import sys


def main():
    """
    After the script connect to the data base it runs the SELECT query
    with the LIKE query to list all states with name starting with N.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY
    'N%' ORDER BY id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
