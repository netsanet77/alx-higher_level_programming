#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                            db=argv[3], port=3306)
    c = datab.cursor()
    c.execute("""SELECT * FROM states WHERE name = '{}' ORDER BY
              states.id ASC""".format(argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
