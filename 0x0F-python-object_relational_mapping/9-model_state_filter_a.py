#!/usr/bin/python3
"""
Script that lists all state objects that contains the letter `a`
from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).filter(State.name.like('%a%')).order_by(
            State.id).all()
    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
