#!/usr/bin/python3
"""
Script that deletes all State object with a name containing the letter a
from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).filter(State.name.like('%a%'))
    for row in rows:
        session.delete(row)
    session.commit()
    session.close()
