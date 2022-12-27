#!/usr/bin/python3
"""
Scripts that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

But the script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            port=3306, db=argv[3])
    c = datab.cursor()
    c.execute("""SELECT * FROM states \
            WHERE name = BINARY %s \
            ORDER BY states.id ASC""", (argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
