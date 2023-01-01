#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            db=argv[3], port=3306)
    c = datab.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    datab.close()
