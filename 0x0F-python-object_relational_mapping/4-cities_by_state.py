#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            db=argv[3], port=3306)
    c = datab.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name \
            FROM cities, states \
            WHERE cities.state_id = states.id \
            ORDER BY cities.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
