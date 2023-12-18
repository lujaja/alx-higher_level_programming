#!/usr/bin/python3
"""This python file contains the class definition of a State and an
    instance Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
