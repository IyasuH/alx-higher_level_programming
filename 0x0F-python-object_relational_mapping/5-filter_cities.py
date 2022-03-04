#!/usr/bin/python3
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s",
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
