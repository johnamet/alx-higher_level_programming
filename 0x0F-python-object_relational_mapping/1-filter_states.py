#!/usr/bin/python3
"""
Lista all states with a name starting with N(upper N)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=passwd,
                         port=3306,
                         database=database)

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states WHERE name\
            LIKE 'N%' ORDER BY id ASC""")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
