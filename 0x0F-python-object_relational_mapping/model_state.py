#!/usr/bin/python3
"""
definition of a State class and an instance Base using sqlalchemy and
links with MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class representation

    __tablename__ (str): the given mysql table
    id (int): the id attribute of the State
    name (str): the name attribute of the State
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
