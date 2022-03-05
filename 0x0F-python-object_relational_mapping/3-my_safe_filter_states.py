#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, it is safe from SQL injections!
"""
import MySQLdb
import sys


def main():
    """
    In this function to make the serach and displaying row from SQL injection
    I use %s instead of {}
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (sys.argv[4], ))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
