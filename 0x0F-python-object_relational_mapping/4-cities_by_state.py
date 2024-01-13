#!/usr/bin/python3
"""
Lista all states with a name starting matching with passed arg
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
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
