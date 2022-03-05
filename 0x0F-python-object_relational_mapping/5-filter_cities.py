#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
And takes 4 arguments where the fourth one is state name
"""
import MySQLdb
import sys


def main():
    """
    This function execute SELECT query to show name of cities in the give state
    And I convert the tuple to list to avoid unnecessary special chars
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id=states.id WHERE states.name=%s""",
                   (sys.argv[4], ))
    result = cursor.fetchall()
    lit = []
    for row in result:
        lit.append(row[0])
    print(", ".join(lit))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
