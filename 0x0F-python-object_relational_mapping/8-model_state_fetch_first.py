#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()
    firstrow = session.query(State).order_by(State.id).first()
    if firstrow:
        print("{}: {}".format(firstrow.id, firstrow.name))
    else:
        print("Nothing")
    session.close()
