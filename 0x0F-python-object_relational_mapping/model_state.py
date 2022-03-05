#!/usr/bin/python3
"""
A python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    Inherits from Base
    links to the MySQL table states
    class attribute id thta represent a column of an auto-genrated,
    unique integer can't be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
