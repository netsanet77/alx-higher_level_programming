#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    result = engine.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = result.fetchall()
    c = 0
    for row in rows:
        print("{}: {}".format(row.id, row.name))
