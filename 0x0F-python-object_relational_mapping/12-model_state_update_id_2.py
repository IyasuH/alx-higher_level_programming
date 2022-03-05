#!/usr/bin/python3
"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    And this script change the name of the state where id = 2 to New Mexico
    with SQLAlchemy ORM
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).filter(State.id == 2):
        inst.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
