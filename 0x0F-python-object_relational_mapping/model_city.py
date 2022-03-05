#!/usr/bin/python3
"""
Similar to model_state And contains class definition of City
"""
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """
    inherits from Base importedfrom model_state
    linkes to MySQL table cities
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string of 128
    characters and can’t be null
    class attribute state_id that represents a column of an integer,
    can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      autoincrement=True, nullable=False)
    UniqueConstraint('id')
