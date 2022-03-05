#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    This function does as the previous (SQLAlchemy ORM) ones
    except that it only dispaly states that contains letter 'a'
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.
                                                  id).filter(State.
                                                             name.
                                                             contains('a')):
        print("{}: {}".format(instance.id, instance.name))

    session.close()


if __name__ == "__main__":
    main()
