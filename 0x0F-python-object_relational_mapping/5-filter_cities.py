#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            db=argv[3], port=3306)
    c = datab.cursor()
    c.execute("""SELECT cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = BINARY %s \
            ORDER BY cities.id ASC""", (argv[4],))
    rows = c.fetchall()
    c = 0
    for row in rows:
        if c != 0:
            print(", ", end="")
        print("%s" % row, end="")
        c += 1
    print()
