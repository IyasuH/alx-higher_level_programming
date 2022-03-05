#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    This function does like task number except this time it just print only the
    for the first row
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if (instance is not None):
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    main()
