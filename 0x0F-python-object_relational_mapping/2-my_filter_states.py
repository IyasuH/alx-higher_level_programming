#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
And the script takes 4 arguments (username, password) for mysql,
database name and state name to be searched
"""
import MySQLdb
import sys


def main():
    """
    This function excute the SELECT query to specific
    row with a given state name
    And it uses 'format' to create the SQL query with the user input
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY
    name = '{}' ORDER BY id ASC"""
                   .format(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
