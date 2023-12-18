#!/usr/bin/python3
"""This python file contains the class definition of a State and an
    instance Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    States class inherits from Base. this class links to the MySQL table states.
    Attributes:
        id: represent column of integer type, pk, can't be null.
        name: column of string type
    """
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
