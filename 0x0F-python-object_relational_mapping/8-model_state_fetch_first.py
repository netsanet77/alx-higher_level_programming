#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    result = engine.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    row = result.fetchone()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print()
