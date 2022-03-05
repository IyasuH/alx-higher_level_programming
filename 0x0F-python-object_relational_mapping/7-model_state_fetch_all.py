#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    In this function to list all state objects
    from the database using SQLAlchemy
    ORM first engine is created and defined
    the usename, password, database name to
    connect with the database then session is created then for loop to list
    all State objects from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    session.close()


if __name__ == "__main__":
    main()
