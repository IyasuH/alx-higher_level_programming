#!/usr/bin/python3
"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
And takes 4 argument ad the forth one is state name to be searched
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    And this function prints state id for the given state as an argument
    And it does that using SQLAlchemy ORM
    """
    n = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).filter(State.name == sys.argv[4]):
        n = 1
    if (n == 1):
        print("{}".format(inst.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
