#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
And the script takes 3 aguments mysql username, mysql password
and database name using sys.argv.
"""
import MySQLdb
import sys


def main():
    """
    Uses MySQLdb module to connect to MySQL on localhost at port 3306
    After it connect to the database it excute
    SELECT query to show all the rows from states table
    ordered by 'id' in ascending order.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
